import cv2
import numpy as np
import mediapipe as mp
import time
import random


mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)


fruit_radius = 30
fruit_color = (0, 0, 255) 
fruit_x = random.randint(100, 540)
fruit_y = 0
fruit_speed = 7
score = 0

prev_time = time.time()
frame_count = 0

with mp_pose.Pose(
    static_image_mode=False,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8,
    model_complexity=2,
    enable_segmentation=False,
    smooth_landmarks=True
) as pose:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  
        h, w, _ = frame.shape

        frame_count += 1
        curr_time = time.time()
        elapsed = curr_time - prev_time
        if elapsed > 1:
            fps = frame_count / elapsed
            prev_time = curr_time
            frame_count = 0

        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)

        right_hand_y = None
        right_hand_x = None

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0,255,0), thickness=4, circle_radius=5),
                mp_drawing.DrawingSpec(color=(0,0,255), thickness=3, circle_radius=4)
            )
            
            right_wrist = results.pose_landmarks.landmark[16]
            right_hand_x = int(right_wrist.x * w)
            right_hand_y = int(right_wrist.y * h)
            
            cv2.circle(frame, (right_hand_x, right_hand_y), 15, (255, 255, 0), -1)

       
        cv2.circle(frame, (fruit_x, fruit_y), fruit_radius, fruit_color, -1)
        fruit_y += fruit_speed

      
        if right_hand_x is not None and right_hand_y is not None:
            dist = np.sqrt((fruit_x - right_hand_x) ** 2 + (fruit_y - right_hand_y) ** 2)
            if dist < fruit_radius + 30:
                score += 1
                fruit_x = random.randint(100, w - 100)
                fruit_y = 0

        
        if fruit_y > h:
            fruit_x = random.randint(100, w - 100)
            fruit_y = 0

      
        cv2.putText(frame, f"Score: {score}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        if 'fps' in locals():
            cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

        cv2.imshow('Catch the Fruit Game (Raise Right Hand!)', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()