# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:17:56 2020

@author: diazd
"""

import numpy as np
import cv2


def distance_to_camera(knownWidth, focalLength, picWidth):
        # compute and return the distance from the maker to the camera
        return (knownWidth * focalLength) / picWidth
    
    
cap = cv2.VideoCapture(0)
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    cv2.imshow('Frame',frame)
    marker = cv2.selectROI("frame", frame, fromCenter=False, showCrosshair=False)
    print(marker)
    print(marker[2])
    picWidth = marker[2]
    
    # initialize the known distance from the camera to paper
    knownDistance = 180.0
    
    # initialize the known paper width
    knownWidth = 75.0
    
    focalLength = (picWidth * knownDistance) / knownWidth
    print("distance focal:",focalLength)
    
    
    print(distance_to_camera(knownWidth, focalLength, picWidth))
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
