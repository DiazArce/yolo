# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:55:46 2020

@author: diazd
"""
import numpy as np
import cv2



def distance_to_camera(f, R, r):
        # compute and return the distance from the maker to the camera
        if (r!=0):
            distance_cm = (f * R) / r
            distance_m = distance_cm/100
            return(distance_cm)
        else:
            print("division by zero");
cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    cv2.imshow('frame', frame)
   
    marker = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=False)
    print(marker)
    print("r",marker[2])
    r = marker[2]
  
    print("r: ",r)
    # initialize the known paper width
    R = 75.0
    print("R: ",R)

    f = 512.32
    
    print("distance: ",distance_to_camera(f, R, r))
 
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
