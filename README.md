<h2>Jarvis-Control-Your-PC-with-your-EYES-Automating-PC
<h4>2nd project
<h3>Title: Eye-Controlled Mouse Script

<h4>Introduction:
<h5This Python script leverages computer vision and facial landmark detection to create an eye-controlled mouse. It uses the OpenCV library for webcam access, the MediaPipe library for face mesh detection, and PyAutoGUI for mouse control. The script allows users to control the mouse cursor based on the movements of their eyes.

<h4>Dependencies:

<h4>OpenCV: 
<h5for capturing video from the webcam.
MediaPipe: for detecting facial landmarks and face mesh.
PyAutoGUI: for controlling the mouse cursor.
Script Overview:

<h4>Video Capture Setup:
<h5 Initialize the webcam using OpenCV's VideoCapture
Create a FaceMesh object from MediaPipe for detecting facial landmarks.
Get the screen size using PyAutoGUI.

<h4> Main Loop:
<h5Continuously capture video frames from the webcam.
Flip the frame horizontally for better user experience.
Convert the frame from BGR to RGB color space.
Process the frame with the face mesh object to detect facial landmarks.

<h4>Eye Tracking:
<h5Extract facial landmarks for the right and left eyes.
Move the mouse cursor to the center of the right eye based on the detected landmark.
Visualize the landmarks on the frame for better understanding.
Check if the left eye is almost closed; if yes, perform a left-click using PyAutoGUI.
Check if the right eye is almost closed; if yes, perform a right-click using PyAutoGUI.

<h4>Display:
<h5Display the processed frame with the overlaid landmarks.
Press the 'Esc' key to exit the script.

<h4>How to Use:
<h5Ensure that Python is installed on your system.
Install the required libraries: opencv-python, mediapipe, and pyautogui.
Save the script with a .py extension.
Run the script using a Python interpreter.
Use the script to control the mouse cursor with your eyes.
Press the 'Esc' key to exit the script.

<h4>Conclusion:
<h5This script demonstrates a simple implementation of eye-controlled mouse functionality using computer vision and Python libraries. Users can interact with the mouse cursor through eye movements, offering a hands-free alternative for certain mouse actions.






