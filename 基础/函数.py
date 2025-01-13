#函数作为参数的时候，不加（）
#当既有位置传参，又有关键字传参的时候，位置传参在前，关键字传参在后 name:song name=song
'''
def get_sum(num):
    s=0
    for i in range(1,num+1):
       s+=i
    print(f"1到{num}的总和是{s}")

get_sum(10)
'''


def happy_birthday(age,name="小敏"):   #位置参数要在默认参数前面
    print('祝'+name+'生日快乐')
    print('祝'+str(age)+'生日快乐')



'''
#个数可变的位置参数
def fun(*para):
    print(type(para))
    for item in para:
        print(item)
#这样是列表成为para元组的一个元素了
lst=[30,20,10]
fun(lst)
fun([22,33,44,55])
#fun(*para:40,30,20)
fun(10)
#在调用是，参数前面加一颗星，分将列表进行解包
#这样是把列表转换为了元组para
fun(*[22,33,44,55])

t=("dami",19,["adea",19,20])
fun(*t)
'''

'''
#个数可变的关键字传参
def fun1(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'___',value)

fun1(name="大米",age=18,height=170)  #这是关键字参数
d={"name":"dami","age":18,"sex":"女"}
#关键字传参这样是错的
#fun1(d)
#进行解包后是对的
fun1(**d)
'''

#函数的返回值
def calc(a,b):
    return a+b
#print(calc(3,4))

#返回多个参数
def calc1(num):
    for i in range(1,num+1):
        odd=0
        even=0
        s=0
        if i%2==0:
            even+=i
        else :
            odd+=i
        s+=i
    return even,odd,s
# print(type(calc1(10)))
# # print(calc1(10))
# a,b,c=calc1(10)
# print(a,b,c)

#global
def calc2(x,y):
    global s #定义和赋值的时候要分开
    s=x+y

#print(calc2(10,20))
#print(s) #s这时候是全局变量

#lambda 匿名函数
s1=lambda a,b:a+b
print(type(s1))
print(s1(10,20))
print('*'*30)
lst=[19,23,45,32]

for i in range(len(lst)):
    result=lambda x:x[i] #根据索引取值
    #print(result(lst))

for i in range(len(lst)):
    result=lambda x:x[i]
    #print(result(lst))

lst1=[
    {'name':'dami','score':89},
    {'name':'ziwen','score':98},
    {'name':'xiaomin','score':100},
]
def sort_dami(a):
    return a['score']

#lst1.sort(key=lambda x:x.get('score'),reverse=True) #降序 reverse默认是升序false
lst1.sort(key=sort_dami)
#print(lst1)

#递归
def fac(n):
    if n==1:
        return 1
    else:
       return n*fac(n-1)

#print(fac(5))


def Fseq(n):
    if n==1 or n==2:
        return 1
    else:
        return Fseq(n-1)+Fseq(n-2)
#print(Fseq(9))


