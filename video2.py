import cv2

#cap = cv2.VideoCapture(0)  эта строка не сработала, заменена строкой ниже
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    success, frame = cap.read()
    cv2.imshow("camera", frame)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
