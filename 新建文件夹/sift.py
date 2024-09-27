import cv2
import matplotlib.pyplot as plt
# 1读取图像
img = cv2.imread(r"E:\PY\study\pythonProject2\images\tv.jpg")
# img = cv2.imread(r"G:\film\DJ\DJ016#001@00.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 2 sift关键点检测
# 2.1实例化sift对象
sift = cv2.SIFT_create()
# 2.2关键点检测: kp关键点信息包括方向，尺度，位置信息，des是关键点的描述符
kp, des = sift.detectAndCompute(gray, None, )
# 2.3在图像上绘制关键点的检测结果
cv2. drawKeypoints(img, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# 3图像显示
plt.figure(figsize=(10, 8), dpi=100)
plt.imshow(img[:, :, ::-1]), plt.title('sift')
plt.xticks([]), plt.yticks([])
plt.show()
