import cv2
import numpy as np

# 【1】载入图像
srcImage1 = cv2.imread(r"E:\PY\study\pythonProject3\tu\book.jpg")

# 定义一个特征检测类对象
sift = cv2.xfeatures2d.SIFT_create(400)
# 调用detect函数检测出SIFT特征关键点，保存在vector容器中
keypoints_1 = sift.detect(srcImage1)

# 绘制特征关键点
img_keypoints_1 = srcImage1.copy()
img_keypoints_1 = cv2.drawKeypoints(srcImage1, keypoints_1, img_keypoints_1, color=(0, 255, 0))

# 显示效果图
cv2.imshow("img_keypoints_1", img_keypoints_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
