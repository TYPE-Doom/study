import cv2
import numpy as np
o = cv2.imread(r"G:\test\images\lena.jpg", cv2.IMREAD_GRAYSCALE)
r = cv2.Canny(o, 100, 200)
cv2.imshow("original", o)
cv2.imshow("result", r)
cv2.waitKey()
cv2.destroyAllWindows()
