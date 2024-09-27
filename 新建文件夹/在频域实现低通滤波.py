import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"G:\test\images\lena.jpg", 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
rows, cols = img.shape  # 掩膜构造
crow, ccol = int(rows/2), int(cols/2)
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
fShift = dftShift*mask  # 滤波
ishift = np.fft.ifftshift(fShift)
ilmg = cv2.idft(ishift)
ilmg = cv2.magnitude(ilmg[:, :, 0], ilmg[:, :, 1])  # 逆傅里叶变换
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('original'), plt.axis('off')
plt.subplot(122), plt.imshow(ilmg, cmap='gray')
plt.title('inverse'), plt.axis('off')
plt.show()
