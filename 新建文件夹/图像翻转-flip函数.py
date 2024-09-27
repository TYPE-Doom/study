import cv2
a = cv2.imread(r"G:\test\actAvatar0-S.png")
b = cv2.flip(a, 1)
cv2.imshow("1", a)
cv2.imshow("fip", b)
cv2.waitKey()
cv2.destroyAllWindows()
