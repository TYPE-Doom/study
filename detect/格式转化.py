import os
import pydicom
import matplotlib.pyplot as plt
# 1.读取DICOM文件
dicom_directory = r"G:\film"    # 原dcm文件路径
output_directory = r"G:\test"    # png图片保存路径
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
# 2.转换DICOM文件
for root, dirs, files in os.walk(dicom_directory):
    for file in files:
        if file.endswith(".dcm"):
            dicom_file_path = os.path.join(root, file)
            ds = pydicom.dcmread(dicom_file_path)
            pixel_array_numpy = ds.pixel_array

            # 3.保存为PNG
            output_path = os.path.join(output_directory, file.replace(".dcm", ".png"))
            plt.imsave(output_path, pixel_array_numpy, cmap='gray')

# 4、将文件夹命名为test，按需替换
os.rename(output_directory, os.path.join(os.path.dirname(output_directory), 'test'))
