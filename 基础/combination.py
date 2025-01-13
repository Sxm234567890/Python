#序列和索引
'''
s="hellobaby"
for i in range(0,9):
    print(i,s[i],end='\t\t')
for i in range(-9,0):
    print(i,s[i],end='\t\t')

'''

'''
s="hellobaby"
print(s[0:5:2]) #起始位置，结束位置，步数
#两者等价
print(s[::-1])
print(s[-1:-9:-1])
print(s+"you")
print("*"*40)

print("e在s中存在吗",('e' in s))
print("e不在s中存在吗",('e' not in s))
print(len(s))
print(max(s))
print(min(s))
print(s.index('e')) #e第一次出现的位置
print(s.count('e'))
'''
'''
#列表
lst=['hello','world',98,100.5]
print(lst)
lst1=list('helloworld')
lst2=list(range(1,10,2))
print(lst2)
print(lst1)
print(lst1+lst2+lst)
print(lst*3)
print(len(lst))
print(max(lst2))
del lst1
'''
#enumerate函数

lst3=["hello","dami",3,7,9]
'''
for i in lst3:
    print(i)

for i in range(0,len(lst3)):
    print(lst3[i])
'''

'''
#index是lst3的序号，(序号的话，第一是1，第二个就是2，后面以此类推，第一个是4，第二个就是5)item是值
for index,item in enumerate(lst3):
    print(index,item)


for index,item in enumerate(lst3,start=1): #start可以省略
#for index,item in enumrate(lst3,1):
    print(index,item,"   ",end='')

#列表的地址没有发生变化
lst1=['hello','world','python']
print(lst1,id(lst1))
lst1.append('sql')
print('增加元素之后：',lst1,id(lst1))
lst1.remove('world')
print('删除元素后',lst1,id(lst1))
lst1.insert(2,20) #在索引为2的位置插入20
lst1.pop(1)
print(lst1,id(lst1))
#清除
lst1.clear()
print(lst1,id(lst1))
lst1=["hello","dami",1,7,5]
#逆向输出
lst1.reverse()
print(lst1)
new_lst=lst1.copy()
print(new_lst,id(new_lst))
new_lst[1]="huimin"


#sort排序只能是同种类型的进行比较
lst2=["hello","dami","Hello","apple"]
lst2.sort()
print("升序",lst2)
lst2.sort(reverse=True)
print('降序',lst2)

#大写比小写的acsii小
lst=["hello","Dami","apple","Niba"]
lst.sort()
print(lst)
#大小写转换
lst.sort(key=str.lower)  #lower  都转换为小写比较
print(lst)
'''
'''
#sorted得到排序新列表，不改变原列表
lst=[2,35,52,23,64]
lst1=["hello","adeam","Adea","deafea","Bede"]
new_lst=sorted(lst)
new_lst=sorted(lst,reverse=True)
print("原列表",lst)
print("升序后",new_lst)
new_lst1=sorted(lst1,key=str.lower)
print("原列表：",lst1)
print("升序后",new_lst1)
'''






















