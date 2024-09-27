import os
import pydicom
import numpy as np
import cv2


def to255(img):     # 归一化到0-255代码
    min_val = img.min()
    max_val = img.max()
    img = (img-min_val)/(max_val-min_val+1e-5)   # 图像归一化
    img = img * 255    # *255
    return img


# 读取原始dcm图像
src = r"G:\film\DJ016#001@00.dcm"
my_dcm = pydicom.dcmread(src)
info18 = my_dcm.WindowCenter
info19 = my_dcm.WindowWidth
info20 = my_dcm.RescaleIntercept
info21 = my_dcm.RescaleSlope
info22 = my_dcm.pixel_array
CT = info21 * info22 + info20

CT_min = info18 - info19/2
CT_max = info18 + info19/2
CT2 = np.clip(CT, CT_min, CT_max)   # 小于min的都等min，大于max的都等于max
ct_image = to255(CT2)    # 归一化
cv2.imwrite("G:/001.png", ct_image)


def all_to_255(img):
    min_val = img.min()
    max_val = img.max()
    img = (img - min_val) / (max_val - min_val + 1e-5)  # 图像归一化
    img = img * 255  # *255
    return img


# 读取DCM
# 原始DCM路径
dcm_folder = r"G:\film"
#
png_folder = r"G:\film\PNG"
#
os.makedirs(png_folder, exist_ok=True)

for filename in os.listdir(dcm_folder):
    if filename.endswith(".dcm"):
        dcm_path = os.path.join(dcm_folder, filename)
        # 读取DCM文件
        my_dcm = pydicom.dcmread(dcm_path)
        info18 = my_dcm.WindowCenter
        info19 = my_dcm.WindowWidth
        info20 = my_dcm.RescaleIntercept
        info21 = my_dcm.RescaleSlope
        info22 = my_dcm.pixel_array
        CT = info21 * info22 + info20

        CT_min = info18 - info19 / 2
        CT_max = info18 + info19 / 2
        CT2 = np.clip(CT, CT_min, CT_max)  # 小于min的都等min，大于max的都等于max
        ct_image = to255(CT2)  # 归一化
        # 构造输出文件路径
        output_path = os.path.join(png_folder, os.path.splitext(filename)[0] + '.png')
        # 保存文件
        cv2.imwrite(output_path, ct_image)

if __name__ == '__main__':
    all_to_255(ct_image)
    # to255()
