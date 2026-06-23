import cv2

img=cv2.imread(r"C:/Users/hp/OneDrive/Pictures/abc.jpg")
width=500
height=400
dim=(width,height)

resized=cv2.resize(img,dim)
cv2.imshow('original',resized)

flipped=cv2.flip(resized,1) #reverse the image horizontally
cv2.imshow('flipped',flipped)

flipped_1=cv2.flip(resized,0) #reverse the image vertically
cv2.imshow('flipped_1',flipped_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

