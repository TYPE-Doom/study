# import numpy as np
# import matplotlib. pyplot as plt
# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()
#
# x = [0, 1, 2, 3, 4, 5, 6]
# y = [0.3, 0.4, 2, 5, 3, 4.5, 4]
# plt.plot(x, y)
# plt.show()
#
# a = [1, 2, 1, 2]
# plt.plot(a, color='r')
# plt.show()

import cv2
import matplotlib.pyplot as plt
o = cv2.imread(r"G:\test\images\lena.jpg")
histb = cv2.calcHist([o], [0], None, [256], [0, 255])
histg = cv2.calcHist([o], [1], None, [256], [0, 255])
histr = cv2.calcHist([o], [2], None, [256], [0, 255])
plt.plot(histb, color='b')
plt.plot(histg, color='g')
plt.plot(histr, color='r')
plt.show()
