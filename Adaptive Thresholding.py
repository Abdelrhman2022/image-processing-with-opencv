# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:00:19 2022

@author: Abdelrahman Ragab
"""

import cv2
import numpy as np
 
# Reading the image from the present directory
image = cv2.imread("images.png", 0)
# Resizing the image for compatibility
image = cv2.resize(image, (500, 600))
 
 
# Ordinary thresholding the same image
_, THRESH_BINARY = cv2.threshold(image, 155, 255, cv2.THRESH_BINARY)
 

#  Adaptive Thresholding MEAN
ADAPTIVE_THRESH_GAUSSIAN = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 199, 5) 
#  Adaptive Thresholding MEAN
ADAPTIVE_THRESH_MEAN = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 199, 5)

# Showing all the three images
cv2.imshow("ordinary threshold", THRESH_BINARY)
cv2.imshow("ADAPTIVE THRESH GAUSSIAN", ADAPTIVE_THRESH_GAUSSIAN)
cv2.imshow("ADAPTIVE THRESH MEAN", ADAPTIVE_THRESH_MEAN)
cv2.waitKey(0)