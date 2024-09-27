import cv2
import matplotlib.pyplot as plt
# 指定TIFF图像文件的路径  
image_path = r"G:\film\DJ\TIF\DJ016#001@00.tif"  # 注意文件扩展名可能是 .tif 或 .tiff

# 使用OpenCV的cv2.imread()函数读取图像  
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
plt.hist(img.ravel(), 256)
plt.figure(figsize=(15, 20), dpi=40)
plt.hist(equ.ravel(), 256)
# plt.show()

cv2.namedWindow('Image Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image Window', 600, 1000)  # 宽度800，高度600
cv2.namedWindow('equ Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('equ Window', 600, 1000)  # 宽度800，高度600
cv2.imshow("Image Window", img)
cv2.imshow("equ Window", equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
