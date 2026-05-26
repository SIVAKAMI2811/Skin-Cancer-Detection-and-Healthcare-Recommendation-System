from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import pickle
import numpy as np
from werkzeug.utils import secure_filename
from preprocess import preprocess_image
from recommend_doctors import get_doctor_recommendations
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Prevent GUI errors
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Set upload folder
UPLOAD_FOLDER = os.path.join('static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load model and label classes
model = pickle.load(open('model.pkl', 'rb'))
label_classes = pickle.load(open('label_classes.pkl', 'rb'))  # array like: ['akiec', 'bcc', ..., 'vasc']

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if '@gmail.com' in email and password:
            session['email'] = email
            return redirect(url_for('index'))
        else:
            flash("Invalid email or password. Make sure to include '@gmail.com'")
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'email' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Preprocess image
            img_array = preprocess_image(filepath)
            if img_array is None:
                flash("Failed to preprocess image.")
                return redirect(url_for('index'))

            # Predict
            prediction = model.predict(img_array)[0]
            predicted_index = np.argmax(prediction)
            predicted_class = label_classes[predicted_index]
            probability = float(prediction[predicted_index])

            # Prepare chart data
            labels = [str(c) for c in label_classes]
            values = [float(round(p * 100, 2)) for p in prediction]

            # Doctor recommendations
            doctors = get_doctor_recommendations(predicted_class)

            return render_template('result.html',
                                   predicted_class=predicted_class,
                                   probability=probability,
                                   labels=labels,
                                   values=values,
                                   doctors=doctors)
    return render_template('index.html')


@app.route("/visualizations")
def visualizations():
    # Path to your metadata CSV
    csv_path = "HAM10000_metadata.csv"  # Change if different

    # Load CSV
    df = pd.read_csv(csv_path)

    # 1. Skin cancer type distribution
    plt.figure(figsize=(6, 6))
    df['dx'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
    plt.title("Distribution of Skin Cancer Types")
    plt.ylabel('')
    img1 = BytesIO()
    plt.savefig(img1, format='png')
    img1.seek(0)
    chart1_url = base64.b64encode(img1.getvalue()).decode()

    # 2. Count plot
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='dx', palette="viridis")
    plt.title("Count of Each Skin Cancer Type")
    plt.xlabel("Disease Type")
    plt.ylabel("Count")
    img2 = BytesIO()
    plt.savefig(img2, format='png')
    img2.seek(0)
    chart2_url = base64.b64encode(img2.getvalue()).decode()

    return render_template(
        "visualizations.html",
        chart1=chart1_url,
        chart2=chart2_url
    )


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
