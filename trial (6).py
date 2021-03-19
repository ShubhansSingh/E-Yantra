import numpy as np
import cv2
loc2=['G:\\yantra\\task 1\\digits\\plus.jpg','G:\\yantra\\task 1\\digits\\minus.jpg']
b=['*','*','*','*','*','*']
d=['*','*','*','*','*','*']
y1=100
y2=200
p=1
image = cv2.imread('G:\\yantra\\task 1\\demo.jpg',0)
while p<5:
    x1=0
    x2=100
    for q in range (0,6):
        img=image[x1:x2 ,y1:y2]
        k=0
        m=0
        n=0
        for i in loc2:
            k=k+1
            temp=cv2.imread(i,0)
            res=cv2.matchTemplate(img,temp,cv2.TM_CCOEFF)
            (vmin,vmax,min,max)=cv2.minMaxLoc(res)
            if vmax >= m :
                m=vmax
                n=k
        if p==1 :
            if n==1 :
                b[q]='+'
            elif n==2 :
                b[q]='-'
        else :
            if n==1 :
                d[q]='+'
            elif n==2 :
                d[q]='-'
        x1=x1+100
        x2=x2+100
    p=p+2
    y1=y1+200
    y2=y2+200
print b
print d
print d[1]
