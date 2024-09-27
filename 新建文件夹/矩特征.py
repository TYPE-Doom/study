import cv2 as cv
# 1图像读取
img = cv.imread(r'E:\PY\study\pythonProject2\images\arrow.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 2计算图像的Hu矩
imgmn = cv.moments(imgray)
imghu = cv.HuMoments(imgmn)
print("图像Hu矩结果:\n", imghu)
# 3计算轮廓的Hu矩
# 3.1转换为二值图
ret, thresh = cv.threshold(imgray, 127, 255, 0)
# 3.2轮廓提取
contours, hierarchy = cv.findContours(thresh, 1, 2)
# 3.3 计算轮廓的Hu矩
cnt = contours[1]
mn = cv.moments(cnt)
hu = cv.HuMoments(mn)
print("Hu矩结果:\n", hu)
