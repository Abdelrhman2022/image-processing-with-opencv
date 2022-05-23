# -*- coding: utf-8 -*-
"""
Created on Tue May 24 00:30:04 2022

@author: Abdelrahman Ragab
"""

import cv2
from matplotlib import pyplot as plt
import numpy as n

#img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('1.png', 0)
_, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal = n.ones((5,5),n.uint8)
dilation = cv2.dilate(mask,kernal,iterations=2)#kernal is the shape which we want to apply such as white square on the circle
erosion = cv2.erode(mask,kernal,iterations=1)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)#dilation + erosion
mg = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernal)#dilation - erpsion
th = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernal)#image - opening

titles = ['image','img','dilation','erosion','opening','closing','mg','th']
images = [img,img,dilation,erosion,opening,closing,mg,th]
plt.figure(8, (14, 8))
for i in range(8):
    plt.subplot(4,4,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()