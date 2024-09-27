import cv2
o = cv2.imread(r"G:\test\images\shape.jpg")
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
co = o.copy()
r = cv2.drawContours(co, contours, -1, (0, 0, 255), 1)
cv2.imshow("original", o)
cv2.imshow("result", r)
cv2.waitKey()
cv2.destroyAllWindows()
