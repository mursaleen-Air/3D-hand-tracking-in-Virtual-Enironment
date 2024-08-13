import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)


#Hand Detector
detector = HandDetector(maxHands=1, detectionCon = 0.8 )

while True:
    #get the frame from the webcam

    success, img = cap.read()
    #hands
    hands, img = detector.findHands(img)
    #landmark values = (x, y, z)* 21
    if hands:
        #get the first hand detected
        hand = hands[0]
        #Get the landmark list
        lmlist = hand['lmlist']
        print(lmlist)
        


    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

