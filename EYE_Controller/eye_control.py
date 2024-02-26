# Import libraries
import cv2 # import the openCv library for computer vision
import mediapipe as mp # import the mediapipe library for face detection & tracking
import pyautogui # import the pyautogui library for controlling the mouse & keyboard



# set up video caption & face mesh 
cam = cv2.Videocaption(0) #create a video caption object to access the webcam
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)# create a face mesh object to detect facial landmarks
screen_w,screen_h = pyautogui.size()#get the screen width & height


# main loop
while True: # loop indefinitely
   _, frame = cam.read() # read a frame from the webcam
   frame = cv2.flip(frame, 1) # flip the frame horizontally
   rgb_frame = cv2.cvtcolor(frame, cv2.COLOR_BGR2RGR) # convert the frame from BGR to RGB color space
   output = face_mesh.process(rgb_frame) # process the frame with the face mesh object
   landmark_points = output.multi_face_landmarks # get list of facial landmarks
   frame_h,frame_w, _ = frame.shape # get the frame height, width & channels  
   
   
   
# Draw landmarks on eyes for better visual understanding 
if landmark_points:# if there are any facial landmarks detected
    landmarks = landmark_points[0].landmark # get the first face's landmarks
    for id , landmark in enumerate(landmarks[474:478]): # loop through th landmarks of the right eye
        x = int(landmarks.x * frame_w) # get the x coordinate of the landmark
        y = int(landmarks.y * frame_h) # get the y coordinate of the landmark
        cv2.circle(frame, (x, y), 3, (0, 255, 0)) # draw a green circle on the frame at the landmark position
        
        
        
        # Move mouse cursor right eye centre
        if id == 1: # if the landmark is the centre of the right eye
            screen_x = screen_w * landmark.x # map the landmark x coordinate to the screen x coordinate 
            screen_y = screen_h * lndmark.y # map the landmark y coordinate to the screen y coordinate 
            pyautogui.moveTo(screen_x, screen_y) # move the mouse cursor to the screen position
    
    
    # Draw left eye landmarks
    left = [landmarks[145],landmarks[159]]# get the landmarks of the left eye corners
    for landmark in left: # get the x coordinate of the landmarks
        x = int(landmark.x * frame_w) # get the x coordinate of the landmark
        y = int(landmark.y * frame_h) # get the y coordinate  of the landmark
        cv2.circle(frame, (x, y), 3, (0, 255, 255)) # draw a yellow circle on the frame at the landmark position
             