import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"G:\test\images\lena.jpg", 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
ishift = np.fft.ifftshift(dftShift)
ilmg = cv2.idft(ishift)
ilmg = cv2.magnitude(ilmg[:, :, 0], ilmg[:, :, 1])
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('original'), plt.axis('off')
plt.subplot(122), plt.imshow(ilmg, cmap='gray')
plt.title('inverse'), plt.axis('off')
plt.show()
