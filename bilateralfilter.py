import cv2

img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")

resize=cv2.resize(img,(500,400))

d=7
sigmacolor=100
sigmaspace=100

b=cv2.bilateralFilter(resize,d,sigmacolor,sigmaspace)
cv2.imshow("OUTPUT",b)
cv2.imshow("Image",resize)
cv2.waitKey(0)
cv2.destroyAllWindows() 
