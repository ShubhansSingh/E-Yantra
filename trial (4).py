import numpy as np
import cv2
img = cv2.imread('G:\\yantra\\task 1\\demo.jpg',0)
temp=cv2.imread('G:\\yantra\\task 1\\digits\\minus.jpg',0)
(w,h)=temp.shape
res=cv2.matchTemplate(img,temp,cv2.TM_CCOEFF)
(vmin,vmax,min,max)=cv2.minMaxLoc(res)
print vmin
print vmax
print min
print max


