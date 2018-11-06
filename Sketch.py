#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 23:46:27 2018

@author: dettrax
"""

import cv2
import numpy as np

def sketch(image):
    #b/w
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
    #REmove noise
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)
    
    #extract edges
    canny_edges = cv2.Canny(img_gray_blur,5,70)
    
    #invert for pencil scetch effect
    _,mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask
 
 
    
cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    
    cv2.imshow('Live image ',frame)
    cv2.imshow('Live sketch ',sketch(frame))
    if(cv2.waitKey(1) == 13 ): # enterkey
        break

cap.release()
cv2.destroyAllWindows()
    
