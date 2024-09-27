import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"G:\test\images\orange.jpg", cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
plt.subplot(121), plt.hist(img.ravel(), 256)
plt.subplot(122), plt.hist(equ.ravel(), 256)
plt.show()
