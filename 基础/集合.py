#{}直接创建集合
#集合是无序的
#集合内是不可变数据类型
s={10,20,30,40}
print(s)
#集合是不可存储列表 列表是不能哈希的
s=set()  #创建一个空集合
print(s)
s={}   #这样创建了一个空字典 ！！！
print(s,type(s))


s=set('helloworld')
print(s)

s2=set([10,20,30])
s3=set(range(1,10))
print('max',max(s3))
print('min',min(s3))
print('len',len(s3))
print('9再集合中存在吗',(9 in s3))
print('9再集合中不存在吗',(9 not in s3))
del s3





