import numpy as np
import cv2
image = cv2.imread('G:\\yantra\\task 1\\demo.jpg',0)
img=image[100:200 ,100:200]
loc=['G:\\yantra\\task 1\\digits\\0.jpg','G:\\yantra\\task 1\\digits\\1.jpg','G:\\yantra\\task 1\\digits\\2.jpg','G:\\yantra\\task 1\\digits\\3.jpg','G:\\yantra\\task 1\\digits\\4.jpg','G:\\yantra\\task 1\\digits\\5.jpg','G:\\yantra\\task 1\\digits\\6.jpg','G:\\yantra\\task 1\\digits\\7.jpg','G:\\yantra\\task 1\\digits\\8.jpg','G:\\yantra\\task 1\\digits\\9.jpg']
for i in loc :
    temp=cv2.imread(i,0)
    res=cv2.matchTemplate(img,temp,cv2.TM_CCOEFF)
    (vmin,vmax,min,max)=cv2.minMaxLoc(res)
    print vmax
    print vmin
