import cv2
import numpy as np

img_rgb = cv2.imread('E:\\demo.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
addr=[]
for i in addr:
 template = cv2.imread(i,0)
 w, h = template.shape[::-1]
 res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
 threshold = 0.55
 loc = np.where( res >= threshold)
 for pt in zip(*loc[::-1]):
  print  pt[1]
template = cv2.imread('E:\\task1_cc\\Task_1_CC\\Experiment\\Task1B_WarmUp\\digits\\plus.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.6
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
 print  pt[1]
