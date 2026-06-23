import cv2
img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")

row=img.shape[0]
column=img.shape[1]

center=(column/2,row/2)
angle=180

r=cv2.getRotationMatrix2D(center,angle,1) #rotation matrix
rotated=cv2.warpAffine(img,r,(column,row))

cv2.imshow("Image",rotated)
cv2.imshow("original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()