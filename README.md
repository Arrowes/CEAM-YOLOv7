## [CEAM-YOLOv7:Improved YOLOv7 Based on Channel Expansion and Attention Mechanism for Driver Distraction Behavior Detection](https://ieeexplore.ieee.org/document/9980374/metrics)
## 项目简介
驾驶员的不规范行为易引发交通事故，因此，为规范驾驶员行为，减少交通事故的发生，对驾驶员行为进行检测至关重要。本文提出了一种改进的目标检测模型CEAM-YOLOv7，该模型利用GAM注意力模块和通道扩展数据增强算法来减少特征图生成过程中的信息丢失，提高检测精度。将YOLOv7架构的Backbone和Head部分加入GAM注意力模块，减少信息损失的同时放大全局维度交互特征，同时，使用剪枝算法，在保证实时检测的前提下，提高了YOLOv7网络的检测性能。此外，使用更适合于实际驾驶场景的红外图像数据集进行训练，结合inversion和CLAHE图像增强方法，提出了一种基于通道扩展的红外图像数据增强算法，改善针对红外图像的目标检测效果。经大量实验结果表明，与YOLOv7相比，CEAM-YOLOv7的map提升了20.26%，FPS达到了156，本文方法的有效性和优越性得到了验证。 

(mydata文件夹中红外数据集不公开，请谅解)
## 技术点
### 通道扩展算法
![图 1](https://raw.sevencdn.com/Arrowes/Arrowes-Blogbackup/main/images/Project1.png)  

```
inversion:通过域迁移的思想使得网络能够更加适应处理后的红外图像。一般用于目标检测所用的 RGB 图像都是白天所摄，通常情况是背景较亮，目标较暗。但驾驶员环境通常较暗，且红外图像成像为辐射特性，背景辐射较弱而目标辐射较强，因此选用 inversion 操作；
CLAHE:由于红外图像的对比度比较低，其灰度分布通常都是分布在较窄的区域，采用自适应直方图均衡化能够使红外图像的灰度分布更均匀，增强对比度的同时抑制噪声，从而达到增加图像细节信息的作用。
```
### GAM注意力机制
![图 2](https://raw.sevencdn.com/Arrowes/Arrowes-Blogbackup/main/images/Project2.png) 

GAM是一种能够捕捉所有三个维度的显著特征的注意机制，采用了CBAM中的顺序通道-空间注意机制，对通道-空间注意力子模块进行了重新设计，通道注意力子模块使用3D置换来跨三维保持信息，使用用两层感知器MLP（Multi-Layer Perceptron）放大跨维信道-空间相关性；空间注意力子模块采用了两个卷积层进行空间信息融合。由此，通过减少信息丢失和放大全局交互特征来提高深度神经网络的性能，提高了对于红外图像目标的识别能力，在识别速度和精度之间进行了有效的权衡，也与数据增强处理中的通道扩展算法相对应。
### 网络架构
![图 3](https://raw.sevencdn.com/Arrowes/Arrowes-Blogbackup/main/images/Project3.png)  

## 实现效果
 ![图 4](https://raw.sevencdn.com/Arrowes/Arrowes-Blogbackup/main/images/Project4.png)  

![图 5](https://raw.sevencdn.com/Arrowes/Arrowes-Blogbackup/main/images/Project5.png)  
