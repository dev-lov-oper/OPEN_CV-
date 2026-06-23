import cv2
import numpy as np

img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")

column=img.shape[1]
row=img.shape[0]

s=np.float32([[1,0,100],[0,1,50]]) #shifting the image to right by 100 and down by 50
shifted=cv2.warpAffine(img,s,(column,row))

cv2.imshow("Image",shifted)
cv2.imshow("original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()