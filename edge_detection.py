#canny edge detection
import cv2
import numpy as np

img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")
resize=cv2.resize(img,(500,400))

min_thrashold=100
max_thrashold=200

edges=cv2.Canny(resize,min_thrashold,max_thrashold)
cv2.imshow("edges",edges)
cv2.imshow("Image",resize)

cv2.waitKey(0)
cv2.destroyAllWindows()

