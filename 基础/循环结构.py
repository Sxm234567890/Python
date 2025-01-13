#range函数，遍历[n,m） 含n,不含m
'''
s=0
for i in range(1,4):
    s+=i
#print在不同的位置是不同的结果
    #print(s)
#print(s)


for i in  'hello':
    print(i)

#水仙花数
#注意 除号的写法是 //
print("水仙花数有")
for i in range(100,1000) :
    first=i//100
    second=i%100//10
    thrid=i%10
    if thrid**3+second**3+first**3==i:
        print(i)

#for_else结构 如果for每一个都遍历成功 执行else
s=0
for i in  range(1,10):
        s+=i
else:
    print(s)
'''

'''
#while循环
#1)初始化变量
#2）条件判断
#3）语句块
#4）改变循环变量

answer=input("今天要上班吗y/n:")
while answer=="y":
    print("好好学习，天天想上")
    answer=input("今天要上班吗y/n:")


s=0
i=1
while i<=100:
    s+=i
    i+=1
#print(s)
else :
     print(s)

'''
'''
i=0
while i<3:
    user_name=input("请输入登陆的用户名")
    passwd=input("请输入用户密码")
    if user_name=="songxiaomin" and  passwd=="12345":
       print("登陆成功")
       i=8
    else:
        print("密码或用户名不正确，您还有",2-i,"次机会")
        i+=1;
if i==3:
   print("你的登陆机会已经用完，登陆失败")
'''
'''
for i in range(1,4):
    for j in range(1,5):
        print("*",end='')
    print("")
    '''
'''
for i in range(1,6):
    j=1
    while j<=i:
          print("*",end="")
          j+=1
    print()
'''
'''
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end='')
    for k in range(1,i*2):
        print("*",end='')
    print()
    '''
'''
#注意整形要加eval
top_row=eval(input("请输入菱形的行数"))
while top_row%2==0:
    top_row=eval(input("输入错误，请重新输入"))

L_row=(top_row+1)//2
for i in range(1,L_row+1):
    for j in range(1, L_row+1- i):
        print(" ", end='')
    for k in range(1, i * 2):
        print("*", end='')
    print()
for i  in range(1,L_row):
    for j in range(1,i+1):
        print(" ",end='')
    for k in range(1,2*(L_row-i)):
        print("*",end='')
    print()
'''

'''
i=0
user_name=input("请输入你的姓名")
passwd=input("请输入你的密码")
while  i<3:
    if user_name=="songxiaomin" and  passwd=="12345":
        print("登陆成功")
        break
    else:
      print("密码或用户名错误")
      print("还剩",2-i,"次机会")
      user_name=input("请输入你的名字")
      passwd=input("请输入你的密码")
      i+=1
else:
    print("登陆次数使用完毕")


i=1
s=0
print("100内的奇数和")
while i<100:
    if  i%2==0 :
        i+=1
        continue
    s+=i
    i+=1
print("s=",s)

#pass 空语句
if True:
    pass # if啥的后面啥也不写的话会报错，但是写pass就不会了
'''
'''
x=2
y=1
min=x if x<y else y
print(min)
'''

for i in range(1,10):
    for j in range(1,i+1):
       # print(i,"*",j,"=",i*j,"  ",end="")
         print(str(j)+"*"+str(i)+"="+str(i*j),end='\t')
    print()













