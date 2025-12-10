import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the pre-trained model
model_path = "classifier.h5"  # Path to your uploaded model
model = load_model(model_path)
print("Model loaded successfully!")

# Define the image size expected by the model
IMG_SIZE = (224, 224)  # Update this if your model requires a different input size

# Dictionary of class labels (Replace with your actual labels)
# Update this dictionary based on how your model was trained
class_labels = {
    0: "Apple",
    1: "Banana",
    2: "Beetroot",
    3: "Bell Pepper",
    4: "Cabbage",
    5: "Capsicum",
    6: "Carrot",
    7: "Cauliflower",
    8: "Chilli Pepper",
    9: "Corn",
    10: "Cucumber",
    11: "Eggplant",
    12: "Garlic",
    13: "Ginger",
    14: "Grape",
    15: "Jalapeno",
    16: "Kiwi",
    17: "Lemon",
    18: "Lettuce",
    19: "Mango",
    20: "Onion",
    21: "Orange",
    22: "Papaya",
    23: "Pear",
    24: "Pineapple",
    25: "Pomegranate",
    26: "Potato",
    27: "Raddish",
    28: "Spinach",
    29: "Sweetcorn",
    30: "Sweet Potato",
    31: "Tomato",
    32: "Turnip",
    33: "Watermelon"
}

class_type = {
    0: "Fruit",
    1: "Fruit",
    2: "Vegetable",
    3: "Vegetable",
    4: "Vegetable",
    5: "Vegetable",
    6: "Vegetable",
    7: "Vegetable",
    8: "Vegetable",
    9: "Vegetable",
    10: "Vegetable",
    11: "Vegetable",
    12: "Vegetable",
    13: "Vegetable",
    14: "Fruit",
    15: "Vegetable",
    16: "Fruit",
    17: "Fruit",
    18: "Vegetable",
    19: "Fruit",
    20: "Vegetable",
    21: "Fruit",
    22: "Fruit",
    23: "Fruit",
    24: "Fruit",
    25: "Fruit",
    26: "Vegetable",
    27: "Vegetable",
    28: "Vegetable",
    29: "Vegetable",
    30: "Vegetable",
    31: "Vegetable",
    32: "Vegetable",
    33: "Fruit"
}

def predict_image(model, image_path, class_labels):
    """
    Predict the class of an input image using the trained model.
    """
    # Load and preprocess the image
    img = load_img(image_path, target_size=IMG_SIZE)  # Resize to match model input
    img_array = img_to_array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make prediction
    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction)  # Get the index of the highest probability

    # Map the predicted index to the class label
    if predicted_index in class_labels:
        predicted_label = class_labels[predicted_index]
        return predicted_label
    else:
        raise ValueError(f"Predicted index {predicted_index} not found in class labels!")

# Path to the test image
image_path = "Images/cucu3.png"  # Replace with the path to your test image

# Predict and print the result
try:
    predicted_label = predict_image(model, image_path, class_labels)
    predicted_type = predict_image(model, image_path, class_type)
    print(f"Fruit or Vegetable: {predicted_type}")
    print(f"The image is classified as: {predicted_label}")
except Exception as e:
    print(f"Error: {e}")
