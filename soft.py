import cv2
import numpy as np

frame = cv2.imread('images/3.jpg')
frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

frame_bin = cv2.threshold(frame_gray, 110, 255, cv2.THRESH_BINARY_INV)[-1]


frame_before = frame_bin
frame_after = cv2.morphologyEx(frame_bin, cv2.MORPH_CLOSE, (3,3), iterations=3)

frame_diff = cv2.bitwise_xor(frame_before, frame_after)

cv2.imshow('before', frame_before)
cv2.imshow('after', frame_after)
cv2.imshow('diff', frame_diff)
cv2.waitKey(0)
cv2.destroyAllWindows()