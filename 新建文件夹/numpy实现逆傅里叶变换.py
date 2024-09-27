import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"G:\test\A0001.png", 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
ishift = np.fft.ifftshift(fshift)   # 移动
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)     # 逆变换
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('original'), plt.axis('off')
plt.subplot(122)
plt.imshow(iimg, cmap='gray')
plt.title('iimg'), plt.axis('off')
plt.show()
