import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

def preprocess_image(img_path, target_size=(64, 64)):
    try:
        img = Image.open(img_path).convert("RGB")
        img = img.resize(target_size)
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)  # ➜ Add batch dimension: (1, 64, 64, 3)
        return img_array
    except Exception as e:
        print(f"Error processing image: {e}")
        return None
