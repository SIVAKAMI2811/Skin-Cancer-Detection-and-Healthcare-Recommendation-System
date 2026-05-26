# Skin-Cancer-Detection-and-Healthcare-Recommendation-System
An AI-powered web application that analyzes skin lesion images and predicts potential skin cancer types using deep learning techniques. The system provides image-based classification, prediction confidence visualization, and healthcare recommendations through an interactive Flask-based interface.
## Dataset
The HAM10000 dataset used for training this skin cancer detection model is hosted on Kaggle because the raw image dataset size exceeds GitHub's upload limits.

* **Dataset Link:** [Download HAM10000 Dataset on Kaggle](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)

### Description
This dataset contains thousands of dermatoscopic images of pigmented skin lesions used for training the deep learning model.
* **Metadata File Included:** `HAM10000_metadata.csv` (already in repository)
* **Image Data Source:** Hosted externally on Kaggle.

### How to Use
1. Click the Kaggle link above to download the image dataset.
2. Extract the images into your local project directory before running `train_model.py` or `app.py`.
