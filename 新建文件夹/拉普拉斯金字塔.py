import cv2
o = cv2.imread(r"G:\test\images\lena.jpg")
od = cv2.pyrDown(o)
odu = cv2.pyrUp(od)
lapPyr = o-odu
o1 = od
o1d = cv2.pyrDown(o1)
o1du = cv2.pyrUp(o1d)
lapPyr1 = o1-o1du
cv2.imshow("lapPyr", lapPyr)
cv2.imshow("lapPry1", lapPyr1)
cv2.waitKey()
cv2.destroyAllWindows()
