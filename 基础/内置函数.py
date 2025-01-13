# print(bool(''))
# print(bool([])) #空列表
# print(bool(list()))
# print(bool(()))  #空元组
# print(bool(tuple()))
# print(bool({}))   #空字典
# print(bool(dict()))
seq=range(1,10)
print(set(seq))

print('商和余数',divmod(12,7))
print('求和',sum([10,123,45]))
print('x的y次幂',pow(2,3))
print(round(3.123412)) #保留整数，四舍五入
print(round(2.123,3))  #保留3位小数
print(round(12.345232,-1)) #保留到十位上

lst=[102,30,10,300,60]
asc_lst=sorted(lst,reverse=True)

new_lst=reversed(lst)  #结果还不是列表
print(type(new_lst))
print(list(new_lst))#只有把new_lst转换为list的时候才能打印

x=['a','b','c','d'] #zip 将对象中的元素打包成元组
y=[10,20,30,40]
z=["dami","dea","honde","deaf"]
zipobj=zip(x,y,z)
print(type(zipobj))
#print(list(zipobj))


enum=enumerate(y,start=1) #从序号1开始匹配
print(type(enum))
print(tuple(enum)) #也需要转换

lst2=[10,20,' ',30]
print(all(lst2))   #false 当列表中有一个元素为false,返回结果就是false
print(all(lst))

print(any(lst2))  #列表中有一个为True，全是True

#print(next(zipobj))  #这个要zipobj还没有遍历的时候使用才有用


#filter
def fun(num):
    return num%2==1
obj=filter(fun,range(10))  #将0-9的整数都执行异常fun操作 经结果为true的放到obj中
print(list(obj))           #记得要转换 list

def upper(x):
    return x.upper()
lst3=['deaf','dgtr','efrg','awde']
obj1=map(upper,lst3)
print(list(obj1))


#format
print(format(3.14,'20'))  #默认右对齐
print(format("hello",'20'))  #默认左对齐
print(format("hello",'*<20')) #<左对齐，*填充符
print(format(20,'b'))  #二进制
print(format(20,'o'))   #八进制
print(format(20,'x'))   #十六进制
print(format(20,'X'))    #十六


print(id(10))


