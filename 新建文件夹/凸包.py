import numpy as np
import cv2
import matplotlib.pyplot as plt
# 1图像读取
img = cv2.imread(r"G:\test\images\shape.jpg")
img1 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 2边缘检测
canny = cv2.Canny(imgray, 127, 255, 0)
# 3轮廓提取
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# 4将轮廓绘制在图像上
img = cv2.drawContours(img, contours, 1, (255, 0, 0), 2)
# 5凸包检测
hulls = []
for cnt in contours:
    # 寻找凸包使用cv2.convexHull(contour)
    hull = cv2.convexHull(cnt)
    hulls.append(hull)
draw_hulls = cv2.drawContours(img1, hulls, -1, (0, 255, 0), 2)
# 6图像显示
plt.figure(figsize=(10, 8), dpi=100)
plt.subplot(121), plt.imshow(img[:, :, ::-1]), plt.title('res1')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(draw_hulls[:, :, ::-1]), plt.title('res2')
plt.xticks([]), plt.yticks([])
plt.show()
