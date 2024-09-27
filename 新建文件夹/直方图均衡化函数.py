import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"G:\test\images\orange.jpg", cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
plt.hist(img.ravel(), 256)
plt.figure()
plt.hist(equ.ravel(), 256)
plt.show()
cv2.imshow("image", img)
cv2.imshow("equ", equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
