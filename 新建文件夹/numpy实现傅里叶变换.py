import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"G:\test\images\lena.jpg", 0)
f = np.fft.fft2(img)    # 傅里叶变换
fshift = np.fft.fftshift(f)     # 移动中心位置
result = 20*np.log(np.abs(fshift))  # 调整值范围
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('original')
plt.axis('off')     # 显示原图
plt.subplot(122)
plt.imshow(result, cmap='gray')
plt.title('result')
plt.axis('off')     # 显示频谱
plt.show()
