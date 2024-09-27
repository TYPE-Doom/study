# import cv2
# import numpy as np
# o = cv2.imread(r"G:\test\actAvatar0-S.png")
# sobelx = cv2.Sobel(o, cv2.CV_64F, 1, 0)
# sobelx = cv2.convertScaleAbs(sobelx)    # 转回uint8
# cv2.imshow("original", o)
# cv2.imshow("x", sobelx)
# cv2.waitKey()
# cv2.destroyAllWindows()

import cv2
import numpy as np
o = cv2.imread(r"G:\test\actAvatar0-S.png", cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(o, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(o, cv2.CV_64F, 0, 1)
sobelx = cv2.convertScaleAbs(sobelx)    # 转回uint8
sobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv2.imshow("original", o)
cv2.imshow("x", sobelx)
cv2.imshow("y", sobely)
cv2.imshow("xy", sobelxy)
cv2.waitKey()
cv2.destroyAllWindows()
