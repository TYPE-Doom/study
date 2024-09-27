import cv2
import numpy as np
a = cv2.imread(r"G:\test\actAvatar0-S.png")
b = cv2.imread(r"G:\test\actWallpaper0-S.png")
result = cv2.addWeighted(a, 0.2, b, 1, 0)
cv2.imshow("a", a)
cv2.imshow("b", b)
cv2.imshow("res", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
