import cv2
img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")

print("dimension of the image is:",img.shape)
scale=50

width=int(img.shape[1]*scale/100)
height=int(img.shape[0]*scale/100)
dim=(width,height)

resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print("dimension of the image is:",resized.shape)

cv2.imshow("Image",resized)
cv2.imshow("original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()