import pydicom
import cv2
import numpy as np


# 读取 DICOM 文件
def read_dicom(filename):
    ds = pydicom.dcmread(filename)
    # 提取图像数据，通常存储在 pixel_array 中
    image_data = ds.pixel_array
    return image_data


# OpenCV 处理图像
def process_image_with_opencv(image_data):
    # OpenCV 默认使用 BGR 格式，但 DICOM 通常是灰度图
    # 如果需要，可以将灰度图转换为伪彩色图（这里不转换）
    # 或者，你可以直接对灰度图进行边缘检测、滤波等操作

    # 示例：使用 OpenCV 的高斯模糊
    blurred_image = cv2.GaussianBlur(image_data, (5, 5), 0)
    cv2.namedWindow('Image Window', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image Window', 600, 1000)  # 宽度800，高度600
    # 显示图像（如果需要）前后名字需要一样
    cv2.imshow('Image Window', blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 主函数
if __name__ == "__main__":
    filename = r"G:\film\DJ016#001@00.dcm"
    image_data = read_dicom(filename)
    process_image_with_opencv(image_data)
