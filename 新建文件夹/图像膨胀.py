import cv2
import numpy as np
# o = cv2.imread(r"G:\test\actAvatar0-S.png", cv2.IMREAD_UNCHANGED)
o = cv2.imread(r"G:\film\DJ\DJ016#001@00-1.png", cv2.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(o, kernel)
cv2.imshow("original", o)
cv2.imshow("dilation", dilation)
cv2.waitKey()
cv2.destroyAllWindows()
