import cv2 as cv
import matplotlib.pyplot as plt
# 1图像和模板读取
img = cv. imread(r"G:\test\images\lena.jpg")
template = cv.imread(r"G:\test\images\temp.png")
h, w, l = template.shape
# 2模板匹配
# 2.1模板匹配
res = cv.matchTemplate(img, template, cv.TM_CCORR)
# 2.2返回图像中最匹配的位置，确定左上角的坐标，并将匹配位置绘制在图像上
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# 使用平方差时最小值为最佳匹配位置
# top_left = min_loc
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
# 3图像显示
# 将一个可能以BGR格式存储的图像调整为RGB格式，以便在Matplotlib中正确显示。
plt.imshow(img[:, :, ::-1])
plt.title('result'), plt.xticks([]), plt.yticks([])
plt.show()
