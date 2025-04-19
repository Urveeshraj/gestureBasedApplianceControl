import cv2
import mediapipe as mp
import time
import controller as cnt

time.sleep(2.0)

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    try:
        while True:
            ret, image = video.read()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            lmList = []

            if results.multi_hand_landmarks:
                for hand_landmark in results.multi_hand_landmarks:
                    myHands = results.multi_hand_landmarks[0]
                    for id, lm in enumerate(myHands.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                    mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
            
            fingers = []
            if len(lmList) != 0:
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1, 5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                total = fingers.count(1)
                cnt.led(total)

                if total == 5:
                    for _ in range(5):
                        cnt.move_servo(180)  # Move servo 5 times
                elif total == 4:
                    for _ in range(4):
                        cnt.move_servo(144)  # Move servo 4 times
                elif total == 3:
                    for _ in range(3):
                        cnt.move_servo(108)  # Move servo 3 times
                elif total == 2:
                    for _ in range(2):
                        cnt.move_servo(72)  # Move servo 2 times
                elif total == 1:
                    for _ in range(1):
                        cnt.move_servo(36)  # Move servo 1 time
                elif total == 0:
                    for _ in range(0):
                        cnt.move_servo(0)  # Move servo 0 times

                if total == 0:
                    cv2.rectangle(image, (20, 300), (300, 425), (0, 0, 0), cv2.FILLED)
                    cv2.putText(
                        image, "0", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5
                    )
                    cv2.putText(
                        image,
                        "LED and 0 Degree",
                        (100, 375),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (255, 0, 0),
                        5,
                    )
                elif total == 1:
                    cv2.rectangle(image, (20, 300), (300, 425), (0, 0, 0), cv2.FILLED)
                    cv2.putText(
                        image, "1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5
                    )
                    cv2.putText(
                        image,
                        "LED and 36 Deg",
                        (100, 375),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (255, 0, 0),
                        5,
                    )
                elif total == 2:
                    cv2.rectangle(image, (20, 300), (300, 425), (0, 0, 0), cv2.FILLED)
                    cv2.putText(
                        image, "2", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5
                    )
                    cv2.putText(
                        image,
                        "LED and 72 Deg",
                        (100, 375),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (255, 0, 0),
                        5,
                    )
                elif total == 3:
                    cv2.rectangle(image, (20, 300), (300, 425), (0, 0, 0), cv2.FILLED)
                    cv2.putText(
                        image, "3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5
                    )
                    cv2.putText(
                        image,
                        "LED and 108 Deg",
                        (100, 375),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (255, 0, 0),
                        5,
                    )
                elif total == 4:
                    cv2.rectangle(image, (20, 300), (300, 425), (0, 0, 0), cv2.FILLED)
                    cv2.putText(
                        image, "4", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5
                    )
                    cv2.putText(
                        image,
                        "LED and 144 Deg",
                        (100, 375),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (255, 0, 0),
                        5,
                    )
                elif total == 5:
                    cv2.rectangle(image, (20, 300), (300, 425), (0, 0, 0), cv2.FILLED)
                    cv2.putText(
                        image, "5", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5
                    )
                    cv2.putText(
                        image,
                        "LED and 180 Deg",
                        (100, 375),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (255, 0, 0),
                        5,
                    )
            
            cv2.imshow("Frame", image)
            k = cv2.waitKey(1)
            if k == ord("q"):
                break

    except KeyboardInterrupt:
        cnt.cleanup()

video.release()
cv2.destroyAllWindows()
