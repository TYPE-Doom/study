import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"G:\test\images\lena.jpg")
plt.hist(img.ravel(), 256)
plt.show()
