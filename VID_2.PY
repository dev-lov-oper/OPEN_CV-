import cv2
from pathlib import Path
import sys

image_path = Path("C:/Users/hp/OneDrive/Pictures/abc.jpg")

if not image_path.exists():
	print(f"Image file not found: {image_path}")
	print("Update image_path to a valid file location.")
	sys.exit(1)

img = cv2.imread(str(image_path))

if img is None:
	print(f"Unable to read image data from: {image_path}")
	sys.exit(1)

cv2.imshow("Image",img)

cv2.waitKey(0)

cv2.destroyAllWindows()