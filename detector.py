# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 18:28:43 2018

@author: Udit
"""

# Face Recognition

# Importing the libraries
import cv2

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')