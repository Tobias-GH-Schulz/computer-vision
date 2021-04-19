import cv2
import mediapipe as mp
import time

video = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(False, 2, 0.5, 0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


while True:
    ret, frame = video.read()

    if ret is not None:
        # convert to rgb because Hands takes rgb image as input
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # get detected hands
        results = hands.process((frameRGB))
        #print(results.multi_hand_landmarks)

        if results.multi_hand_landmarks:
            for handLMS in results.multi_hand_landmarks:
                for id, lm in enumerate(handLMS.landmark):
                    #print(id, lm)
                    h, w, c = frame.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    print(id, cx, cy)
                    if id == 4:
                        cv2.circle(frame, (cx,cy), 15, (255,0,255), cv2.FILLED)

                mpDraw.draw_landmarks(frame, handLMS, mpHands.HAND_CONNECTIONS)


        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (255, 0, 255), 1)

        cv2.imshow("frame", frame)
        cv2.waitKey(1)

        if cv2.waitKey(30) & 0xFF == ord('q'):
                    break
    else:
        break

video.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
