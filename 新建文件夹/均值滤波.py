import cv2
o = cv2.imread(r"G:\test\actAvatar0-S.png")
r = cv2.blur(o, (5, 5))     # 第一个5是宽度，列数。第二个是高度，行数
cv2.imshow("original", o)
cv2.imshow("result", r)
cv2.waitKey()
cv2.destroyAllWindows()