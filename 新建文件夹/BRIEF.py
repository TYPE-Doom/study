import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"E:\PY\study\pythonProject2\images\arrow.png", 0)
# Initiate STAR detector
star = cv2.FeatureDetector_create("STAR")
# Initiate BRIEF extractor
brief = cv2.DescriptorExtractor_create("BRIEF")
# find the key points with STAR
kp = star.detect(img, None)
# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)
print(brief.getInt('bytes'))
print(des.shape)
