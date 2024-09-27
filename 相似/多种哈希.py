import cv2
import numpy as np


# 均值哈希算法
def aHash(img):
    # 缩放为8*8
    img = cv2.resize(img, (8, 8), interpolation=cv2. INTER_CUBIC)
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # s为像素和初值为0，hash_str为hash值初值为''
    s = 0
    hash_str = ''
    # 遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s = np.sum(gray)
    # 求平均灰度
    avg = s/64
    # 灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                hash_str = hash_str+'1'
            else:
                hash_str = hash_str+'0'
    return hash_str


# 差值感知算法
def dHash(img):
    # 缩放8*8
    img = cv2.resize(img, (9, 8), interpolation=cv2.INTER_CUBIC)
    # 转换灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hash_str = ''
    # 每行前一个像素大于后一个像素为1，相反为e，生成哈希
    for i in range(8):
        for j in range(8):
            if gray[i, j] > gray[i, j+1]:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + 'e'
    return hash_str


# Hash值对比
def cmpHash(hash1, hash2):
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n+1
    return n


img1 = cv2.imread(r"E:\PY\study\pythonProject2\tu\book.jpg")
img2 = cv2.imread(r"E:\PY\study\pythonProject2\tu\book2.jpg")
hash1 = aHash(img1)
hash2 = aHash(img2)
print(hash1)
print(hash2)
n = cmpHash(hash1, hash2)
print('均值哈希算法相似度:' + str(n))

hash1 = dHash(img1)
hash2 = dHash(img2)
print(hash1)
print(hash2)
n = cmpHash(hash1, hash2)
print('差值哈希算法相似度:' + str(n))

"""
    均值哈希
缩放：图片缩放为8*8，保留结构，出去细节。
灰度化：转换为256阶灰度图。
求平均值：计算灰度图所有像素的平均值。
比较：像素值大于平均值记作1，相反记作0，总共64位。
生成hash：将上述步骤生成的1和0按顺序组合起来既是图片的指纹（hash）。顺序不固定。但是比较时候必须是相同的顺序。
对比指纹：将两幅图的指纹对比，计算汉明距离，即两个64位的hash值有多少位是不一样的，不相同位数越少，图片越相似。

    差值哈希算法
1. 缩放：图片缩放为8*9，保留结构，出去细节。
2. 灰度化：转换为256阶灰度图。
3. 求平均值：计算灰度图所有像素的平均值。
4. 比较：像素值大于后一个像素值记作1，相反记作0。本行不与下一行对比，每行9个像素，八个差值，有8行，总共64位
5. 生成hash：将上述步骤生成的1和0按顺序组合起来既是图片的指纹（hash）。顺序不固定。但是比较时候必须是相同的顺序。
6. 对比指纹：将两幅图的指纹对比，计算汉明距离，即两个64位的hash值有多少位是不一样的，不相同位数越少，图片越相似。

    Hash值对比
由于返回值为str字符串，所以直接遍历字符串进行比对。
"""