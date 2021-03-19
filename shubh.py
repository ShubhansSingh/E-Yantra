import cv2
import numpy as np
from array import *
image = cv2.imread('G:\\yantra\\sets\\task1_img_7.jpg',0)
x1=0
x2=100
ele=[]
loc=['G:\\yantra\\task 1\\digits\\0.jpg','G:\\yantra\\task 1\\digits\\1.jpg','G:\\yantra\\task 1\\digits\\2.jpg','G:\\yantra\\task 1\\digits\\3.jpg','G:\\yantra\\task 1\\digits\\4.jpg','G:\\yantra\\task 1\\digits\\5.jpg','G:\\yantra\\task 1\\digits\\6.jpg','G:\\yantra\\task 1\\digits\\7.jpg','G:\\yantra\\task 1\\digits\\8.jpg','G:\\yantra\\task 1\\digits\\9.jpg','G:\\yantra\\task 1\\digits\\plus.jpg','G:\\yantra\\task 1\\digits\\minus.jpg']
for p in range (0,6):
    ele.append([])
    y1=0
    y2=100
    for q in range (0,5):
        img=image[x1:x2 ,y1:y2]
        k=-1
        m=0
        n=0
        for i in loc:
            k=k+1
            temp=cv2.imread(i,0)
            res=cv2.matchTemplate(img,temp,cv2.TM_CCOEFF)
            (vmin,vmax,min,max)=cv2.minMaxLoc(res)
            if vmax >= m :
                m=vmax
                n=k
        if n<=9:
            ele[p].append(n)
        else :
            if n==10 :
                ele[p].append('+')
            else :
                ele[p].append('-')
        y1=y1+100
        y2=y2+100
    x1=x1+100
    x2=x2+100
for i in ele :
    s=0
    if i[1]=='+':
        s=i[0]+i[2]
    else :
        s=i[0]-i[2]
    if i[3]=='+':
        s=s+i[4]
    else :
        s=s-i[4]
    i.append(s)
print ele
