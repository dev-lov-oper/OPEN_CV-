import cv2
import numpy as np
# adding shapes and text on the image   

img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")    
cv2.line(img,(0,0),(150,150),(255,0,0),7) #draw a line on the image
img=np.zeros(shape=(600,800,3),dtype=np.uint8) #create a black image

cv2.rectangle(img,(15,25),(200,150),(0,255,0),5) #draw a rectangle on the image
cv2.circle(img,(400,50),30,(0,0,255),5) #draw a circle on the image

pts_polygon=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32) #draw a polygon on the image
cv2.polylines(img,[pts_polygon],True,(0,255,255),5)
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,"Hello",(300,200),font,3,(255,255,0),2,cv2.LINE_AA) #write text on the image

cv2.imshow('shapes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
