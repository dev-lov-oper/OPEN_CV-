import cv2

video = cv2.VideoCapture(
    "C:/Users/hp/OneDrive/Videos/WhatsApp Video 2025-05-29 at 17.13.41_8f4f1640.mp4"
)

while video.isOpened():

    ret, frame = video.read()

    if not ret:
        break

    frame = cv2.resize(frame, (500, 400))

    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()