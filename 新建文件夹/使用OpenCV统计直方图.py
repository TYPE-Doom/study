import cv2
img = cv2.imread(r"G:\test\images\lena.jpg")
hist = cv2.calcHist([img], [0], None,
                    [256], [0, 255])
print(type(hist))
print(hist.size)
print(hist.shape)
print(hist)
