import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# 1图像读取
img = cv.imread(r"G:\test\images\shape.jpg")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 2转换为二值图
ret, thresh = cv.threshold(imgray, 127, 255, 0)
# 3轮廓提取
contours, hierarchy = cv.findContours(thresh, 1, 2)
# 4将轮廓绘制在图像上
img = cv.drawContours(img, contours, 0, (0, 0, 255), 1)
cnt = contours[0]
# 5最小外接圆
(x, y), radius = cv.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
imgRect = cv.circle(img, center, radius, (0, 255, 0), 2)
# 6椭圆拟合
ellipse = cv.fitEllipse(cnt)
img2 = cv.ellipse(img, ellipse, (0, 255, 255), 2)
# 7直线拟合
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv.fitLine(cnt, cv.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img3 = cv.line(img, (cols-1, righty), (0, lefty),
               (0, 255, 0), 2)
# 8图像显示
plt.figure(figsize=(10, 8), dpi=100)
plt.imshow(imgRect[:, :, ::-1]), plt.title('circle')
plt.imshow(img2[:, :, ::-1]), plt.title('ellipse')
plt.imshow(img3[:, :, ::-1]), plt.title('line')
plt.xticks([]), plt.yticks([])
plt.show()
