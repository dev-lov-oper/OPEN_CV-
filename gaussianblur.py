import cv2
img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")

resized=cv2.resize(img,(500,400))

ksize=(7,7)
sigmax=0
sigmay=0
 

blurred=cv2.GaussianBlur(resized,ksize,sigmax,sigmay)
cv2.imshow("blur_Image",blurred)
cv2.imshow("Image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
