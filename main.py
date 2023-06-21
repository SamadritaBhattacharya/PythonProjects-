import cv2
import mediapipe as mp
import pyautogui

cap= cv2.VideoCapture(0)
hd=mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
scrwidth, scrheight = pyautogui.size()
index_y=0
while True:
    _,frame = cap.read()
    frame = cv2.flip(frame,1)
    fheight,fwidth,_ = frame.shape
    rgb_frame= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hd.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x= int(landmark.x*fwidth)
                y= int(landmark.y*fheight)
                pyautogui.moveTo(x,y)

                if id == 8:
                    cv2.circle(img=frame, center=(x,y) , radius=10,color=(0,255,255))
                    index_x = scrwidth/fwidth*x
                    index_y = scrheight/fheight*y
                    pyautogui.moveTo(index_x, index_y)
                     # for index finger
                if id == 4:
                    cv2.circle(img=frame, center=(x,y) , radius=10,color=(0,255,255))
                    thumb_x = scrwidth/fwidth*x
                    thumb_y = scrheight/fheight*y
                    print(abs(index_y-thumb_y))     #for thumb finger
                    if abs(index_y-thumb_y)<20:
                        pyautogui.click()
                        pyautogui.sleep(1)


    cv2.imshow('Virtual mouse' , frame)
    cv2.waitKey(1)

