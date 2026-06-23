import cv2

cap=cv2.VideoCapture(0)
# 0 : for webcam
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        cv2.imshow("video",frame)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
cv2.destroyAllWindows()