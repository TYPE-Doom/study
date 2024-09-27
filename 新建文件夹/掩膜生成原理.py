import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r"G:\test\images\lena.jpg", 0)   # 0表示以灰度值形式读取
mask = np.zeros(image.shape, np.uint8)
mask[100:300, 100:300] = 255
mi = cv2.bitwise_and(image, mask)
cv2.imshow('original', image)
cv2.imshow('mask', mask)
cv2.imshow('mi', mi)
cv2.waitKey()
cv2.destroyAllWindows()
