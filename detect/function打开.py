import pydicom
import matplotlib.pyplot as plt


def display_dicom_image(filename):
    # 读取DICOM文件
    ds = pydicom.dcmread(filename)
    print(ds)
    # 检查图像数据是否存在,ds = pydicom.dcmread(filename)
    if 'PixelData' in ds:
        # 提取图像数据
        image_data = ds.pixel_array

        # DICOM图像有时可能是多帧的，但焊缝胶片可能是单帧的
        # 这里我们假设它是单帧的，并直接显示

        # 显示图像
        plt.figure(figsize=(20, 20))  # 调整图像大小以更好地显示
        plt.imshow(image_data, cmap='gray')  # 使用灰度色彩映射
        plt.title('DICOM Weld Image')
        plt.axis('off')  # 关闭坐标轴
        plt.show()

        # 缩小影像
        data_downsampling = ds.pixel_array[::4, ::4]
        # 将缩小的影像放入原来的 DICOM 数据集
        ds.PixelData = data_downsampling.tobytes()
        # 更新影像大小
        ds.Rows, ds.Columns = data_downsampling.shape
        # 另存 DICOM 文件
        ds.save_as("de-identification.dcm")

    else:
        print("DICOM file does not contain image data.")

filename = r"G:\film\DJ016#001@00.dcm"

# 显示DICOM图像
display_dicom_image(filename)
