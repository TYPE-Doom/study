import subprocess
import sys


def open_image(image_path):
    # 根据不同的操作系统调用不同的图片查看器
    if sys.platform == "win32":
        # 使用Windows的图片和传真查看器
        subprocess.run([r"G:\fiji-win64\Fiji.app\ImageJ-win64.exe", image_path])
    else:
        print("不支持的操作系统")

    # 使用Popen获取输出和错误
    # process = subprocess.Popen([r"G:\fiji-win64\Fiji.app\ImageJ-win64.exe"],
    #                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # out, err = process.communicate()
    # print(out)
    # print(err)


image_path = r"G:\film\DJ016#001@00.dcm"
open_image(image_path)
