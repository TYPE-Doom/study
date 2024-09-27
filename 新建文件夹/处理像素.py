# import cv2
# img = cv2.imread(r"G:\test\actAvatar0-S.png")   # 读取
# cv2.namedWindow("test")     # 创建窗口
# cv2.imshow("test", img)     # 展示
# cv2.waitKey(0)  # 等待状态
# cv2.destroyAllWindows()     # 销毁窗口
# cv2.imwrite(r"G:\test\A0001.png", img)  # 保存
# import cv2
# img = cv2.imread(r"G:\test\actAvatar0-S.png", cv2.IMREAD_UNCHANGED)   # 读取
# cv2.imshow("original", img)     # 展示
# img[10:50] = [255]
# cv2.imshow("result", img)     # 展示
# cv2.waitKey(0)  # 等待状态
# cv2.destroyAllWindows()     # 销毁窗口


import cv2
import numpy as np
i = cv2.imread(r"G:\test\actAvatar0-S.png", cv2.IMREAD_UNCHANGED)   # 读取
print(i.item(100, 100, 0))
i[100, 100, 0] = 255
print(i.item(100, 100, 0))
# cv2.imshow("original", i)     # 展示
# cv2.imshow("result", i)     # 展示
# cv2.waitKey(0)  # 等待状态
# cv2.destroyAllWindows()     # 销毁窗口
