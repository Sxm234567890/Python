import random
d={item:random.randint(a=1,b=100) for item in range(4)} #键是0-3 值是1-100中的任意值
print(d)

lst=[1001,1002,1003]
lst2=['陈梅梅','王一一','李累']
d={key:value for key,value in zip(lst,lst2)}
print(d)