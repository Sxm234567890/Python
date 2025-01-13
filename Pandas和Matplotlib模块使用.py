import  pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('jd手机销售数据.xlsx')
# print(df)
#编码方式转换
plt.rcParams['font.sans-serif']=['SimHei']
#设置画布
plt.figure(figsize=(10,6))
labels=df['商品名称']
y=df['北京出库数量']
# print(labels)
# print(y)

#绘制饼图
plt.pie(y,labels=labels,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('2028年1月北京各手机品牌出库量占比')
#显示
plt.show()