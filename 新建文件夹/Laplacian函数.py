import cv2
import numpy as np
o = cv2.imread(r"G:\test\actAvatar0-S.png", cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Laplacian(o, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)  # 转回uint8
cv2.imshow("original", o)
cv2.imshow("laplacian", laplacian)
cv2.waitKey()
cv2.destroyAllWindows()
