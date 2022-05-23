# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:05:49 2022

@author: Abdelrahman Ragab
"""

import cv2
import numpy as np

image = cv2.imread('images.png', 0)

image = cv2.resize(image, (512, 512))




_ , BINARY = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)


_ , BINARY_INV = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY_INV)


_ , TRUNC = cv2.threshold(image, 200, 255, cv2.THRESH_TRUNC)


_ , TOZERO = cv2.threshold(image, 200, 255, cv2.THRESH_TOZERO)


_ , TOZERO_INV = cv2.threshold(image, 200, 255, cv2.THRESH_TOZERO_INV)




cv2.imshow("BINARY", BINARY)
cv2.imshow("BINARY_INV", BINARY_INV)
cv2.imshow("TRUNC", TRUNC)
cv2.imshow("TOZERO", TOZERO)
cv2.imshow("TOZERO_INV", TOZERO_INV)

cv2.waitKey(0)