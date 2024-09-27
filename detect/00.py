import cv2
import numpy as np
import matplotlib.pyplot as plt


def equalizehist_16to8(file_path):
    # 读取16位PNG图像
    img = cv2.imread(file_path, -1)

    # 检查图像是否成功读取并且是16位
    if img is not None and img.dtype == np.uint16:
        print("Image loaded as 16-bit.")
    else:
        print("Error loading image or image is not 16-bit.")
        exit()

    # 将16位图像转换为8位图像
    img_8bit = (img / 256).astype(np.uint8)

    # 应用直方图均衡化
    img_eq = cv2.equalizeHist(img_8bit)
    return img_8bit, img_eq


def plt_show(img_8bit, img_eq):
    # 绘制并显示原始8位图像和均衡化后图像的直方图
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.hist(img_8bit.ravel(), bins=256, range=[0, 255])
    plt.title('Original 8-bit Histogram')
    plt.subplot(1, 2, 2)
    plt.hist(img_eq.ravel(), bins=256, range=[0, 255])
    plt.title('Equalized 8-bit Histogram')
    plt.show()


def cv2_show(img_8bit, img_eq):
    # 显示原始8位图像和均衡化后的图像
    cv2.imshow('Original 8-bit Image', img_8bit)
    cv2.namedWindow('Image Window', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image Window', 200, 1500)  # 宽度800，高度600
    cv2.imshow('Image Window', img_eq)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    file_path = r"G:\film\DJ016#001@00.png"
    img_8bit, img_eq = equalizehist_16to8(file_path)
    plt_show(img_8bit, img_eq)
    cv2_show(img_8bit, img_eq)


