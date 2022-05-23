# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:42:27 2022

@author: Abdelrahman Ragab
"""


import cv2
import numpy as np
 
# Reading the image from the present directory
image = cv2.imread("images.png", 0)
# Resizing the image for compatibility
image = cv2.resize(image, (500, 600))
 
# The initial processing of the image
# image = cv2.medianBlur(image, 3)

 
# The declaration of CLAHE
# clipLimit -> Threshold for contrast limiting
clahe = cv2.createCLAHE(clipLimit = 5)
final_img = clahe.apply(image) + 30
 
# Ordinary thresholding the same image
_, ordinary_img = cv2.threshold(image, 155, 255, cv2.THRESH_BINARY)
 


# Showing all the three images
cv2.imshow("ordinary threshold", ordinary_img)
cv2.imshow("CLAHE image", final_img)
cv2.waitKey(0)