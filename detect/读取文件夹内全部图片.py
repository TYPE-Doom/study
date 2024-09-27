import os
import subprocess


def open_images_in_folder(folder_path):
    # 确保提供的路径是一个有效的目录  
    if not os.path.isdir(folder_path):
        print(f"错误：{folder_path} 不是一个有效的目录。")
        return

        # 遍历目录中的所有文件
    for filename in os.listdir(folder_path):
        # 构建文件的完整路径  
        file_path = os.path.join(folder_path, filename)

        # 检查文件是否是图片（这里以.jpg, .jpeg, .png为例）  
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            # 尝试使用默认程序打开图片  
            # 注意：这个命令在Windows和macOS/Linux上可能不同  
            if os.name == 'nt':  # Windows  
                os.startfile(file_path)
            else:  # macOS/Linux，这里使用xdg-open作为示例  
                try:
                    subprocess.run(['xdg-open', file_path])
                except FileNotFoundError:
                    print(f"无法找到xdg-open来打开文件 {file_path}")


folder_path = 'D:\桌面壁纸\Error'  # 替换为你的图片文件夹路径
open_images_in_folder(folder_path)
