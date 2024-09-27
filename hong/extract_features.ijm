// 打开一张图像
open("G:/film/DJ016#001@00.png");

// 获取当前图像的标题
title = getTitle();

// 计算图像的平均亮度
run("Measure");
avgBrightness = getResult("Mean", nResults-1);

// 将结果保存到文本文件中
resultFile = File.open("G:/film/result.txt");
print(resultFile, "Image: " + title);
print(resultFile, "Average Brightness: " + avgBrightness);
File.close(resultFile);

// 关闭图像
close();