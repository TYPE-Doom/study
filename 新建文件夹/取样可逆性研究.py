import cv2
o = cv2.imread(r"G:\test\images\lena.jpg")
up = cv2.pyrUp(o)
down = cv2.pyrDown(up)
diff = down-o
cv2.imshow("up", up)
cv2.imshow("down", down)
cv2.imshow("difference", diff)
cv2.waitKey()
cv2.destroyAllWindows()
