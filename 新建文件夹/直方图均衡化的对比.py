import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"G:\test\images\lena.jpg", cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
plt.subplot(221)
plt.imshow(img, cmap='gray'), plt.axis('off')
plt.subplot(222)
plt.imshow(equ, cmap='gray'), plt.axis('off')
plt.subplot(223)
plt.hist(img.ravel(), 256)
plt.subplot(224)
plt.hist(equ.ravel(), 256)
plt.show()
