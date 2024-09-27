import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"G:\film\DUIJ\DUIJIE8-40#001@00.png", -1)
img_8bit = (img / 256).astype(np.uint8)
blurred = cv2.GaussianBlur(img_8bit, (3, 3), 0)
equ = cv2.equalizeHist(blurred)
plt.hist(equ.ravel(), bins=256, range=[0, 255])
plt.title('Equalized 8-bit Histogram')
plt.show()
r, b = cv2.threshold(equ, 150, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(b, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
co = img.copy()
c = cv2.drawContours(co, contours, -1, (0, 0, 255), 2)
cv2.namedWindow('Image Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image Window', 200, 1000)
cv2.imshow("Image Window", c)
cv2.waitKey()
cv2.destroyAllWindows()

# 高斯滤波、直方图均衡化、反截断阈值


# import cv2
# import matplotlib.pyplot as plt
# o = cv2.imread(r"G:\film\DJ016#001@00.png")
# histb = cv2.calcHist([o], [0], None, [256], [0, 255])
# histg = cv2.calcHist([o], [1], None, [256], [0, 255])
# histr = cv2.calcHist([o], [2], None, [256], [0, 255])
# plt.plot(histb, color='b')
# plt.plot(histg, color='g')
# plt.plot(histr, color='r')
# plt.show()
