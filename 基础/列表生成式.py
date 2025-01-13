import random
'''
lst=[item for item in range(1,11)]

lst=[item*item for item in range(1,11)]

#for 里面不想要就写_，要的话就写i啥的
lst1=[random.randint(a=1,b=100) for _ in range(10)] #生成1-100的10个整数
print(lst1)

lst2=[i for i in range(10) if i%2==0 ]
print(lst2)
'''
lst=[
    ["城市","环比","同比"],
    ["北京","102","103"],
    ["上海","104","205"]
]
print(lst)

for row in lst:
    for item in row:
        print(item,end='\t')
    print()

lst1=[[j for j in range(5)]for i in range(4)]
print(lst1)










