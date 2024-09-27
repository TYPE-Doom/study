import cv2
a = cv2.imread(r"G:\test\actAvatar0-S.png")
b = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
cv2.imshow("a", a)
cv2.imshow("gray", b)
cv2.waitKey()
cv2.destroyAllWindows()