import cv2
import numpy as np

img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")
width=600
height=400

dim=(width,height)
resized=cv2.resize(img,dim)

kernal=np.ones((5,5),np.uint8)

# erosion=cv2.erode(resized,kernal,iterations=1)

# dialation=cv2.dilate(resized,kernal,iterations=1)
# opening=cv2.morphologyEx(resized,cv2.MORPH_OPEN,kernal)
# closing=cv2.morphologyEx(resized,cv2.MORPH_CLOSE,kernal)
# gradient=cv2.morphologyEx(resized,cv2.MORPH_GRADIENT,kernal)
top_hat=cv2.morphologyEx(resized,cv2.MORPH_TOPHAT,kernal)
black_hat=cv2.morphologyEx(resized,cv2.MORPH_BLACKHAT,kernal)

cv2.imshow("Image",resized)
# cv2.imshow("Erosion",erosion)
# cv2.imshow("Dilation",dialation)
# cv2.imshow("Opening",opening)
# cv2.imshow("Closing",closing)
# gradient =dialation-erosion
# cv2.imshow("Gradient",gradient)
cv2.imshow("Top Hat",top_hat)
cv2.imshow("Black Hat",black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
