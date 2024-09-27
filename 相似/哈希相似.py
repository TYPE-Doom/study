from PIL import Image
import imagehash

# # 加载图片
# image = Image.open("path/to/your/image.jpg")
#
# # 计算图片的哈希值，这里使用average_hash算法
# hash = imagehash.average_hash(image)
#
# # 打印哈希值
# print(hash)

# 如果你想比较两个图片的哈希值，可以这样做：  
hash1 = imagehash.average_hash(Image.open(r"E:\PY\study\pythonProject2\tu\book.jpg"))
hash2 = imagehash.average_hash(Image.open(r"E:\PY\study\pythonProject2\tu\book2.jpg"))
print(hash1)
print(hash2)
# 计算两个哈希值之间的差异  
diff = hash1 - hash2

# 打印差异值  
print(diff)
