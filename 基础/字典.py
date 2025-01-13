'''
d={20:'dog',20:'cat',30:'zoo',10:'pig'} #10：dog 覆盖了10：cat  后面的会覆盖前面的
print(d)

lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','cat']
zipobj=zip(lst1,lst2)
print(zipobj)
#print(list(zipobj))
d=dict(zipobj)  #zipobj是一个映射对象，转换为字典
print(d)

d=dict(cat=10,dog=20)
print(d)


t=(10,20,30)
print({t:10})  #元组可以作为键

#t=[10,20,30]  #列表不可以，因为列表是可变的
#print({t:10})


#字典属于序列
print('max',max(d))
print('min',min(d))
print("长度",len(d))
'''
'''
#字典元素的访问和遍历
d={'hello':10,'daemi':30,'huimi':20}
#如果key不存在，d['hello']会报错，d,get('hello')会显示空
print(d['hello'])
print(d.get('hello'))
print(d.get('hello','不存在'))
for item in d.items():
    print(item)

for key,value in d.items():
     print(key,'---->',value)

'''


'''
#获取keys
d={1002:'pig',1003:'dog',1004:'cat'}
d[1005]='zoo'
print(d.keys())
keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))
print(d.values())

lst=list(d.items())
print(lst)    #字典转换为列表，列表里的元素是元组


print(d.pop(1002)) #把键对应的值拿到，然后把这个键对值删除
print(d.pop(1008,'不存在'))
print(d.popitem()) #随机从字典里取出键值对，如果是元组就删除
print(d)

d.clear()
print(d)
print(bool(d))
'''

