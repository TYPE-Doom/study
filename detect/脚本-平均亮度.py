import subprocess

# ImageJ的安装路径
imagej_path = r"G:\fiji-win64\Fiji.app\ImageJ-win64.exe"

# 宏脚本的路径
macro_path = r"E:\PY\study\pythonProject2\hong\extract_features.ijm"

# 调用ImageJ并运行宏脚本
subprocess.run([imagej_path, "-macro", macro_path])

# 此时，ImageJ应该已经执行了宏脚本，并将结果保存到了指定的文本文件中
