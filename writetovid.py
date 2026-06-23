import cv2

video = cv2.VideoCapture(
    "C:/Users/hp/OneDrive/Videos/WhatsApp Video 2025-05-29 at 17.13.41_8f4f1640.mp4"
)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('output.mp4', fourcc, 25.0, (1920, 1080))

while video.isOpened(): 
    
    ret, frame = video.read()
    if ret:
        output.write(frame)
        cv2.imshow("video", frame)

    if cv2.waitKey(10) & 0xFF == ord('s'):
        break

    

cv2.destroyAllWindows()