import cv2
import numpy as np
from array import *
image = cv2.imread('G:\\yantra\\sets\\task1_img_7.jpg',0)
y1=0
y2=100
a=[0,0,0,0,0,0]
c=[0,0,0,0,0,0]
e=[0,0,0,0,0,0]
b=['*','*','*','*','*','*']
d=['*','*','*','*','*','*']
e1=[0,'*',0,'*',0,0]
e2=[0,'*',0,'*',0,0]
e3=[0,'*',0,'*',0,0]
e4=[0,'*',0,'*',0,0]
e5=[0,'*',0,'*',0,0]
e6=[0,'*',0,'*',0,0]
ele=[e1,e2,e3,e4,e5,e6]
p=0
loc1=['G:\\yantra\\task 1\\digits\\0.jpg','G:\\yantra\\task 1\\digits\\1.jpg','G:\\yantra\\task 1\\digits\\2.jpg','G:\\yantra\\task 1\\digits\\3.jpg','G:\\yantra\\task 1\\digits\\4.jpg','G:\\yantra\\task 1\\digits\\5.jpg','G:\\yantra\\task 1\\digits\\6.jpg','G:\\yantra\\task 1\\digits\\7.jpg','G:\\yantra\\task 1\\digits\\8.jpg','G:\\yantra\\task 1\\digits\\9.jpg']
loc2=['G:\\yantra\\task 1\\digits\\plus.jpg','G:\\yantra\\task 1\\digits\\minus.jpg']
while p<5:
    x1=0
    x2=100
    for q in range (0,6):
        img=image[x1:x2 ,y1:y2]
        k=-1
        m=0
        n=0
        for i in loc1:
            k=k+1
            temp=cv2.imread(i,0)
            res=cv2.matchTemplate(img,temp,cv2.TM_CCOEFF)
            (vmin,vmax,min,max)=cv2.minMaxLoc(res)
            if vmax >= m :
                m=vmax
                n=k
        if p==0 :
            a[q]=n
        elif p==2:
            c[q]=n
        else :
            e[q]=n
        x1=x1+100
        x2=x2+100
    p=p+2
    y1=y1+200
    y2=y2+200
y1=100
y2=200
p=1
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



