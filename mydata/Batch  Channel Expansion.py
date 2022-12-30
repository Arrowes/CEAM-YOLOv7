from PIL import Image
import os

import cv2

path = os.getcwd()  # 获取当前路径
file_list = os.listdir()
for file in file_list:
    filename = os.path.splitext(file)[0]
    filexten = os.path.splitext(file)[1]
    if filexten == '.jpg':
        image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        c1 = image

        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        c2 = clahe.apply(c1)

        c3 = 255 - c1
        image = cv2.merge([c1, c2, c3])
        img = Image.fromarray(image)
        img.save(file)
