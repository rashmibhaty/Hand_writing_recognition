# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:03:31 2020

@author: rashmibh
"""

import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_cv = cv2.imread("1.png")

#Get the gray scale image
img = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

#Filter noise
(thresh, img) = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
img=cv2.blur(img,(2,2))

print("string: ")
print(pytesseract.image_to_string(img))

cv2.imshow("Image", img)
cv2.waitKey(0) 
