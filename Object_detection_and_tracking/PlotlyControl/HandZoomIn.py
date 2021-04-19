import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
import math
import numpy as np
import osascript



video = cv2.VideoCapture(0)
detector = htm.handDetector(min_detection_confidence=0.7)
while True:
    ret, frame = video.read()

    if ret is not None:
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame, draw=False)
        if len(lmList) != 0:
            #print(lmList[4], lmList[8])
        
            # get the x,y coordinates for the tip of the thumb 
            x1, y1 = lmList[4][1], lmList[4][2]
            # get the x,y coordinates for the tip of the second finger
            x2, y2 = lmList[8][1], lmList[8][2]

            # get center of distance between the two tips
            cx, cy = (x1+x2)//2, (y1+y2)//2

            # draw bigger circles on the two tips
            cv2.circle(frame, (x1,y1), 15, (255,0,255), cv2.FILLED)
            cv2.circle(frame, (x2,y2), 15, (255,0,255), cv2.FILLED)

            # draw line between the two tips
            cv2.line(frame, (x1,y1), (x2,y2), (255,0, 255), 3)

            # draw a circle at the center of the distance between the two tips
            cv2.circle(frame, (cx,cy), 15, (255,0,255), cv2.FILLED)

            # use hypothenuse function to get distance between the two tips
            lenght = math.hypot(x2-x1, y2-y1)
            
            # Hand range 50 - 300
            # volume range 1 - 100

            
            x_eye = np.interp(lenght, [50, 400], [0, 6.26])
            print(int(lenght), xe)
            #osascript.osascript(f"set volume output volume {vol}")



            if lenght<50:
                # change color of circle at the center of the distance 
                # between the two tips to green
                cv2.circle(frame, (cx,cy), 15, (0,255,0), cv2.FILLED)

        cv2.imshow("frame", frame)
        cv2.waitKey(1)

        if cv2.waitKey(30) & 0xFF == ord('q'):
                    break
    else:
        break

video.release()
cv2.destroyAllWindows()
cv2.waitKey(1)