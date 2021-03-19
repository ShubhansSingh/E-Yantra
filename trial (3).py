import numpy as np
import cv2
img = cv2.imread('G:\\yantra\\task 1\\demo.jpg',0)
s=img[200:300, 400:500]
print s.shape
cv2.imshow('image',s)
cv2.waitKey(0)
cv2.destroyAllWindows()

