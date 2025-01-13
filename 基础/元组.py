#不可变数据类型，没有增删查改
#除了元组外，列表，集合，字典都是可变数据类型
'''
t=('hello',[10,20,30],'python','world')  #列表可以作为元组的元素，反之也可
print(t)

t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)

print('10在元组t中存在？',(10 in t))
print('10不在元组中存在？',(10 not in t))
print(max(t))
print(min(t))
print(t.count(10))
print(t.index(10))
print(len,len(t))

#如果元组中只要一个元素,一定要加一个逗号
t=(10,)
print(t,type(t))
del t
'''
t=('hello','dami','nihao')
print(t[0])
t1=t[1::2]
print(t1)
for item in t:
    print(item)

for i in  range(len(t)):
   print(i,t[i])
#enumerate
for index,temp in enumerate(t):
    print(index,"---->",temp)

'''
t=(i for i in range(1,4))
print(id(t))
t=tuple(t)
print(id(t))
for item in t:
    print(item,end=" ")
for item in t:
    print(item,end=" ")
'''

#生成器里面的值被取完后再转换成元组，元组里面就没数了
t=(i for i in range(4)) #t是生成器
print(t)
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())

t=tuple(t)   #t转换成了元组
print(t)