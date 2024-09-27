import cv2
import numpy as np
a = cv2.imread(r"G:\test\actAvatar0-S.png")
b = np.ones((80, 80, 3))
b = a[60:120, 70:140]
# a[0:60, 0:70] = b
cv2.imshow("ori", a)
cv2.imshow("res", b)
cv2.waitKey(0)
cv2.destroyAllWindows()

