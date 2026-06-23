import cv2

img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")

cv2.imshow("Image",img)
cv2.imwrite('car.jpg', img)
cv2.waitKey(0)

cv2.destroyAllWindows()