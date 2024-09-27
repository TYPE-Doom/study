# import cv2
# import numpy as np
# a = cv2.imread(r"G:\test\actAvatar0-S.png")
# b, g, r = cv2.split(a)
# cv2.imshow("test", a)
# cv2.imshow("t", b)
# m = cv2.merge([b, g, r])
# cv2.imshow("merge", m)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 另一种模式
import cv2
import numpy as np
a = cv2.imread(r"G:\test\actAvatar0-S.png")
rows, cols, chn = a.shape
b = cv2.split(a)[0]
r = np.zeros((rows, cols), a.dtype)
g = np.zeros((rows, cols), a.dtype)
m = cv2.merge([b, g, r])
cv2.imshow("merge", m)
cv2.waitKey(0)
cv2.destroyAllWindows()
