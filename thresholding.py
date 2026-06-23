import cv2
import numpy as np

img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")

threshold_value=127

binary_threshold=cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)

# THRESH_BINARY : If the pixel value is greater than the threshold value, it is set to 255 (white), otherwise it is set to 0 (black).
cv2.imshow("original",img)
cv2.imshow("binary_threshold",binary_threshold[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
