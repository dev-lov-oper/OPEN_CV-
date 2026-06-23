import cv2

img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")
print("dimension of the image is:",img.shape)
cv2.imshow("Image",img)

cv2.waitKey(0)

cv2.destroyAllWindows()