import cv2
img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")

resize=cv2.resize(img,(500,400))
kernel=3
blur=cv2.medianBlur(resize,kernel)
cv2.imshow("blur_Image",blur)
cv2.imshow("Image",resize)
cv2.waitKey(0)
