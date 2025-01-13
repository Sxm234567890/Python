# from PIL import Image
# #加载图片
# im=Image.open('google.png')
# #print(type(im),im)
# # 提取RGB图像的颜色通道，返回结果是图像的副本
# r,g,b=im.split()
# print(r)
# print(g)
# print(b)
# #合并通道
# om=Image.merge(mode='RGB',bands=(r,b,g))
# om.save('logo.jpg')


#RGBA和RGB是两种常见的图像颜色模式，它们之间的主要区别在于是否包含透明度信息。
# from PIL import Image
# im = Image.open('google.png')  # 确保路径正确
# print(im.mode)  # 打印图像模式
# if im.mode == 'RGB':
#     r, g, b = im.split()
# elif im.mode == 'RGBA':   #A是表示透明度信息  JPEG格式不支持透明度信息。(.jpg)
#     channels= im.split()  # 处理RGBA图像
#     r,g,b=channels[0:3]
#     om=Image.merge(mode='RGB',bands=(r,b,g))
#     om.save('google.jpg')
# else:
#     print("图像模式不是RGB或RGBA")
#     # 你可以在这里添加代码来转换图像模式，或者处理错误情况

from PIL import Image
im=Image.open('google.png')
r,g,b,a=im.split()
om=Image.merge(mode='RGBA',bands=(r,a,b,g))
om.save('google1.png')






