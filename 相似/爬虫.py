import requests
from lxml import etree

url = "https://www.qmkan.cc/book/13657/"    # 设置个urL变量，变量为url地址
req = requests.get(url)     # 申请地址数据
list_page = etree.HTML(req.text)    # 解析数据，用于操作
txt_name = list_page.xpath("//h1/text()")[0]    # 获取书名
file_name = f'./{txt_name}.txt'
# 定义本地存储名称
list_a = list_page.xpath("//dd/a//@href")[0:]     # 提取所有章节页
list_a = [url+i for i in list_a]     # 拼接所有章节页完整链接

for i in list_a:
    # 循环所有章节页
    req = requests.get(i)   # 申请章节页数据
    data_page = etree.HTML(req. text)   # 解析整个页面的数据
    data_title = data_page.xpath("//h1/text()")[0]     # 提取章节页名称
    data_list = data_page.xpath("//div[@id='content']/text()")[0:]  # 提取所有小说内容
    data = "\n".join(data_list)  # 拼接小说内容
    this_chapter = f"\n{data_title}\n{data}"  # 拼接标题与内容
    with open(file=file_name, mode="a", encoding='UTF-8') as f:  # 本地新建文件
        f.write(this_chapter)  # 将小说内容写入文件
    print(f'{data_title}--下载完成! ')  # 打印下载
