#图像的灰度处理
import numpy as np
import matplotlib.pyplot as plt
#读取图片
n1=plt.imread('go.jpg')
print(type(n1),n1)  #数组，三纬数组。最高维度表示的是图像的高。次纬度表示的二十图像的宽，最第维[R,G,B]颜
#显示图片  imshow用于在坐标轴上显示图像数据
plt.imshow(n1)
plt.show()
#编写一个灰度公式
n2=np.array([0.299,0.587,0.114])  #创建数组
#将数组n1(RGB)颜色与数组n2(灰度公式固定值),进行点乘运算
x=np.dot(n1,n2)
#传入数组,显示灰度
# 通过指定cmap='gray'，
# 您明确告诉plt.imshow()：“这些值已经是灰度值了，请使用灰度颜色映射来显示它们
plt.imshow(x,cmap='gray')
#显示图像
plt.show()

# plt.imshow()负责在内存中设置图像数据，
# 而 plt.show() 负责将这些数据渲染到屏幕上。
# 通常，你会先使用 plt.imshow() 来加载和显示图像，
# 然后使用 plt.show() 来实际查看它。在编写绘图代码时，这两个函数经常一起使用。