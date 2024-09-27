# import cv2
# import numpy as np
# o = cv2.imread(r"G:\test\actAvatar0-S.png")
# scharry = cv2.Scharr(o, cv2.CV_64F, 0, 1)
# scharry = cv2.convertScaleAbs(scharry)    # 转回uint8
# cv2.imshow("original", o)
# cv2.imshow("y", scharry)
# cv2.waitKey()
# cv2.destroyAllWindows()

import cv2
import numpy as np
o = cv2.imread(r"G:\test\actAvatar0-S.png", cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Scharr(o, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(o, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
cv2.imshow("original", o)
cv2.imshow("x", scharrx)
cv2.imshow("y", scharry)
cv2.imshow("xy", scharrxy)
cv2.waitKey()
cv2.destroyAllWindows()
