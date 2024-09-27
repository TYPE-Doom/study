import cv2
import numpy as np
a = cv2.imread(r"G:\test\actAvatar0-S.png")
b = a
add1 = a+b
add2 = cv2.add(a, b)
cv2.imshow("test", a)
cv2.imshow("1", add1)
cv2.imshow("2", add2)
cv2.waitKey(0)
cv2.destroyAllWindows()
