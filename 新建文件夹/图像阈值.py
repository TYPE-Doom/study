import cv2
a = cv2.imread(r"G:\test\actAvatar0-S.png", cv2.IMREAD_UNCHANGED)
r, b = cv2.threshold(a, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("a", a)
cv2.imshow("b", b)
cv2.waitKey()
cv2.destroyAllWindows()

# import cv2
# a = cv2.imread("image\\lena512.bmp", cv2.IMREAD_UNCHANGED)
# r,b = cv2.threshold(a, 127, 255, cv2.THRESH_TRUNC)
# cv2.imshow("a", a)
# cv2.imshow("b", b)
# cv2.waitKey()
# cv2.destroyAllWindows()
