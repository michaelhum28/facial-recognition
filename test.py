import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()

    if not success:
        print("Error: Failed to capture frame.")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
