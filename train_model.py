import os
import numpy as np
import pandas as pd
import cv2
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import pickle
from tqdm import tqdm

# Constants
IMAGE_FOLDER = 'HAM10000_images'  # Folder where merged images are stored
CSV_FILE = 'HAM10000_metadata.csv'  # CSV file with metadata
IMAGE_SIZE = 64  # Resize all images to 64x64

# Load metadata
df = pd.read_csv(CSV_FILE)

# Encode target labels
le = LabelEncoder()
df['label'] = le.fit_transform(df['dx'])
labels = df['label'].values
num_classes = len(le.classes_)

# Save label classes for decoding later
with open('label_classes.pkl', 'wb') as f:
    pickle.dump(le.classes_, f)

# Load and preprocess images
images = []
for image_id in tqdm(df['image_id']):
    image_path = os.path.join(IMAGE_FOLDER, f"{image_id}.jpg")
    if os.path.exists(image_path):
        img = cv2.imread(image_path)
        img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
        images.append(img)
    else:
        print(f"Missing image: {image_path}")
images = np.array(images)
images = images.astype('float32') / 255.0  # Normalize

# One-hot encode labels
labels = to_categorical(labels, num_classes)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Build CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
