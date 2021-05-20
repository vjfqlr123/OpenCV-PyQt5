import cv2
import numpy as np

src = cv2.imread('../opencv_data/aspalt.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv2.GaussianBlur(src, ksize = (7,7), sigmaX = 0.0)
eg = cv2.Canny(dst, 50, 200)
eg2 = cv2.Canny(dst, 0, 200)
eg3 = cv2.Canny(dst, 0, 255)

cv2.imshow('eg', eg)
cv2.imshow('eg2', eg2)
cv2.imshow('eg3', eg3)
cv2.waitKey()
cv2.destroyAllWindows()