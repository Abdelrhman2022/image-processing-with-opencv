# -*- coding: utf-8 -*-
"""
Created on Tue May 24 21:04:53 2022

@author: Abdelrahman Ragab
"""

import cv2
import numpy as n
from matplotlib import pyplot as plt

#homogeneous filter each ouput pixel is the mean(kernal)


img = cv2.imread('image.png')
img = cv2.resize(img, (512,512))
#opencv take BGR
#matplotlib take RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = n.ones((2,2),n.float32)/25
#LPF remove noise n blur
#HPF find edges
dat = cv2.filter2D(img, 0, kernel)
blur = cv2.blur(img, (5,5));
gblur = cv2.GaussianBlur(img,(5,5),0)#remove the high frequency noise
median = cv2.medianBlur(img, 5)#replace pixel value with its site pixels, work fine with salt n pepper noise kernal size % 2 != 0
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)#remove noise by preserving edge

titles = ['image','2c','blur','gblur','median','bilateralFilter']
images = [img,dat,blur,gblur,median,bilateralFilter]
#gaussian filter pixel in the between are high weight n in the outlines wight is small


for i in range(6):
    plt.subplot(4,4,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
