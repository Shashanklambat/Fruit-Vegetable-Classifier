import cv2
import numpy as np
import tensorflow as tf

# Load your trained model
model = tf.keras.models.load_model('classifier.h5')
print("Model loaded successfully!")

# Define your labels manually
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

# Function to preprocess the frame
def preprocess_frame(frame):
    # Resize to match the input shape of the model
    resized_frame = cv2.resize(frame, (224, 224))
    # Normalize pixel values to match model input range
    normalized_frame = resized_frame / 255.0
    # Expand dimensions to add batch size
    input_frame = np.expand_dims(normalized_frame, axis=0)
    return input_frame

# Start video capture
camera = cv2.VideoCapture(2)

if not camera.isOpened():
    print("Error: Could not open the camera.")
    exit()

print("Press 'q' to exit.")
while True:
    ret, frame = camera.read()
    if not ret:
        print("Error: Unable to capture frame.")
        break

    # Flip the frame horizontally for a mirror-like view
    frame = cv2.flip(frame, 0)

    # Preprocess the frame for prediction
    input_frame = preprocess_frame(frame)

    # Get prediction from the model
    prediction = model.predict(input_frame)
    label_index = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    # Map the predicted index to the corresponding label
    label = class_labels.get(label_index, "Unknown")

    # Display the prediction and confidence on the frame
    cv2.putText(frame, f"{label} ({confidence:.2f}%)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame with prediction
    cv2.imshow("Live Camera Prediction", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
camera.release()
cv2.destroyAllWindows()
