import numpy as np
import cv2

img = cv2.imread('face6.jpg')
fgbg = cv2.BackgroundSubtractorMOG2()

#ret, frame = img.read()

fgmask = fgbg.apply(img)
cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.imshow('frame',fgmask)
cv2.waitKey(0)
