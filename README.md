# 📦 Fruit & Vegetable Image Classifier
=========================================

A deep learning–based image classification project that identifies **fruits** and **vegetables** from images. This model can classify input images, run predictions on sample images, and even recognize fruits/vegetables using a **live camera feed**.


# 🧠 Project Overview
======================
This project uses a trained neural network model (`classifier.h5`) to classify different fruits and vegetables.

You can:

- ✔ Test classification on sample images  
- ✔ Provide your own image and get predictions  
- ✔ Use your webcam for real-time fruit/vegetable recognition  
---


# 📁 Project Structure
------------------------

Fruit_Vegetable_Classifier/
│
├── classifier.h5 # Trained model
├── image_check.py # Script: classify a single image
├── live_camera_check.py # Script: real-time classification via webcam
├── requirements.txt # Python dependencies
│
└── Images/ # Sample test images
├── apple.png
├── banana.png
├── cauliflower.png
└── cucumber.png


# 🚀 How to Run the Project
-----------------------------

### **1\. Install Dependencies**

Make sure Python 3.8+ is installed.

Install required libraries:

**pip install -r requirements.txt**


### 2\. Run Image Classification on a File ###
------------------------------------------

**python image_check.py**

You will be prompted to enter the path of an image.Example input:

Enter image path: Images/apple.png

Output will show predicted fruit/vegetable name.

### 3\. Real-Time Classification with Webcam ###
--------------------------------------------

**python live_camera_check.py**

A webcam window will open and predictions will appear in real time.

🧪 **Model Details**
--------------------

*   Format: **Keras .h5 model**
    
*   Type: **Convolutional Neural Network**
    
*   Training dataset: **Fruit and vegetable image dataset**
    
*   Output: Classified label among supported categories
    

📦 **Dependencies**
-------------------

Your requirements.txt contains all necessary libraries. Typical dependencies include:

*   TensorFlow / Keras
    
*   NumPy
    
*   OpenCV
    
*   Pillow
    
*   Matplotlib
    

Install using:

**pip install -r requirements.txt**


# 🖼 Sample Prediction Images
---------------------------

The Images/ folder contains sample test images:

*   Apple
    
*   Banana
    
*   Cauliflower
    
*   Cucumber
    
You can replace or add more images to test the classifier.


# 🎯 Future Improvements
--------------------------

Potential upgrades:

*   Add mobile app interface
    
*   Expand dataset and accuracy
    
*   Deploy as a web app (Flask/Streamlit)
    
*   Use TensorFlow Lite for edge devices
    

# 👤 Author
-------------

**Shashank Lambat**  
Fruit & Vegetable Classifier Project  
Feel free to contribute or open an issue!
