# 导入需要的库
from PIL import Image  # 用于图像处理
import os  # 用于文件操作
import cv2  # OpenCV 库，用于图像处理和计算机视觉任务
 
# 获取当前工作目录
path = os.getcwd()
 
# 获取当前目录下的所有文件列表
file_list = os.listdir()
 
# 遍历文件列表
for file in file_list:
    # 获取文件名和扩展名
    filename = os.path.splitext(file)[0]
    filexten = os.path.splitext(file)[1]
 
    # 如果是 JPG 格式的图片
    if filexten == '.jpg':
        # 读取图像并将其转换为灰度图像
        image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        c1 = image
 
        # 创建 CLAHE 对象并应用它来增强对比度
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        c2 = clahe.apply(c1)
 
        # 取反灰度图像
        c3 = 255 - c1
 
        # 将三个灰度通道合并成彩色图像
        image = cv2.merge([c1, c2, c3])
 
        # 将处理后的图像保存为原始文件名
        img = Image.fromarray(image)
        img.save(file)
