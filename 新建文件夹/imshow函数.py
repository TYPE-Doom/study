import cv2
import matplotlib.pyplot as plt
o = cv2.imread(r"G:\test\images\orange.jpg")
g = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
plt.subplot(221)
plt.imshow(o)
plt.axis('off')
plt.subplot(222)
plt.imshow(o, cmap='gray')
plt.axis('off')
plt.subplot(223)
plt.imshow(g)
plt.axis('off')
plt.subplot(224)
plt.imshow(g, cmap='gray')  # 这个才是正确的,想要的
plt.axis('off')
plt.show()

import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"G:\test\images\orange.jpg")
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])
plt.subplot(121)
plt.imshow(img), plt.axis('off')
plt.subplot(122)
plt.imshow(img2), plt.axis('off')
plt.show()
