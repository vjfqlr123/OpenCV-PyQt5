import cv2
import numpy as np

src = cv2.imread('../opencv_data/aspalt.jpg', cv2.IMREAD_GRAYSCALE)
eg = cv2.Canny(src, 200, 255)
#1
fastF = cv2.FastFeatureDetector.create(threshold = 30)
kp = fastF.detect(eg)
dst = cv2.drawKeypoints(eg, kp, None, color = (0,0,255))
print('len(kp)=', len(kp))

#2
fastF.setNonmaxSuppression(False)
kp2 = fastF.detect(eg)
dst2 = cv2.drawKeypoints(eg, kp2, None, color = (0,0,255))
print(len(kp2))
cv2.imshow('dst2', dst2)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()