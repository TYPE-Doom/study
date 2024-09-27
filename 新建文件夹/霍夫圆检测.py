import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
# 1读取图像，并转换为灰度图
planets = cv.imread(r"E:\PY\study\pythonProject2\images\star.png")
gay_img = cv.cvtColor(planets, cv.COLOR_BGRA2GRAY)
# 2进行中值模糊，去噪点(霍夫圆检测对噪声敏感)
img = cv.medianBlur(gay_img, 7)
# 3霍夫圆检测
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 200,
                          param1=100, param2=50, minRadius=0, maxRadius=100)
circles = np.uint16(np.around(circles))     # 变成循环可以识别利用的int类型
# 4将检测结果绘制在图像上
for i in circles[0, :]:  # 遍历矩阵每一行的数据
    # 绘制圆形
    cv.circle(planets, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # 绘制圆心
    cv.circle(planets, (i[0], i[1]), 2, (0, 0, 255), 3)
# 5图像显示
plt.figure(figsize=(10, 8), dpi=100)
plt.imshow(planets[:, :, ::-1]), plt. title('round detect')
plt.xticks([]), plt.yticks([])
plt.show()
