# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:43:26 2022

@author: Abdelrahman Ragab
"""

import cv2
import numpy as np

# Callback Function for Trackbar (but do not any work)
def nothing(*arg):
    pass



# Code here
def SimpleTrackbar(Image, WindowName):
 # Generate trackbar Window Name
 TrackbarName = WindowName + "Trackbar"

 # Make Window and Trackbar
 cv2.namedWindow(WindowName)
 cv2.createTrackbar(TrackbarName, WindowName, 0, 255, nothing)

 Image = cv2.resize(Image, (512,512))

 # Allocate destination image
 Threshold = np.zeros(Image.shape, np.uint8)

 # Loop for get trackbar pos and process it
 while True:
  # Get position in trackbar
  TrackbarPos = cv2.getTrackbarPos(TrackbarName, WindowName)
  # Apply threshold
  cv2.threshold(Image, TrackbarPos, 255, cv2.THRESH_BINARY, Threshold)
  # Show in window
  cv2.imshow(WindowName, Threshold)

  # If you press "ESC", it will return value
  ch = cv2.waitKey(5)
  if ch == 27:
      break

 cv2.destroyAllWindows()
 return Threshold


image = cv2.imread('images.png', 0)
SimpleTrackbar(image, "THRESH_BINARY")