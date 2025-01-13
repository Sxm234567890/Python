import random
#题一
'''
lst=[88,89,90,98,00,99]
print(lst)
'''
'''
for i in range(0,len(lst)):
    if str(lst[i])!='0':
        lst[i]='19'+str(lst[i])
    else:
        lst[i]='200'+str(lst[i])
print(lst)
'''
'''
for index,values in enumerate(lst):
    if str(values) != '0':
        lst[index] = '19' + str(values)
    else:
        lst[index] = '200' + str(values)
print(lst)
'''
'''
#题二
Thing=[]
for i in range(5):
    thing=input("请输入商品的编号和商品的名称")
    Thing.append(thing)
for item in Thing:
    print(item)

cart=[]
while True:
    BuytH=input("请输入你要购买的商品")
    if BuytH=='q':
        break;
    flag=False
    for i in Thing:
        if BuytH==i[0:3]:
           flag=True
           cart.append(BuytH)
           break
    if flag==False:
        print("没有你需要的商品")
cart.reverse()
for i in cart:
    print(i)
    '''
'''
#题二第二种做法
Thing=[]
for _ in range(5):
    input_data=input("请输入商品的编号和商品的名称(用空格分隔)：")
    number,name=input_data.split()
    Thing.append((number,name))
cart=[]
while True:
    BuytH=input("请输入你要购买的商品（按q退出）")
    if BuytH=='q':
        break
    flag=False
    for number,name in Thing:
        if BuytH==number:
            cart.append((number,name))
            flag=True
            break
    if not flag:
        print("没有你需要的商品")

cart.reverse()
for number,name in cart:
    print(f"购买的商品编号是{number},购买的商品名称是{name}")
'''
'''
dict_ticket={
     'G1569':['北京南-天津南','19:01','18.20','19:29'],
     'G1256':['北京南-长春西','18:01',"14:00","12:20"],
     'G1378':['北京南-杭州西','12:00',"13:00","14:10"]
}
print('车次  出发站-到达站      出发时间        到达时间        历时时长')
for key in dict_ticket.keys():
    print(key,end='')
    for item in dict_ticket.get(key):
        print(item,end='\t\t')
    print()
Trips=input("请输入你要乘坐的车次")
info=dict_ticket.get(Trips,'车次不存在')
if info!='车次不存在':
       people=input("请输入要乘坐的乘客（多位乘客使用逗号分隔）")
       s=info[0]+info[1]+'开'
       print("你已经购买"+Trips+',请'+people+'尽快换取纸质车示')
else:
    print("您购买的车次不存在")

s='helloPython,HelloJava.hellophp'
word=input("请输入你要统计的字符")
print('{2}在{0}中出现的次数：{1}'.format(s,s.lower().count(word),word))
'''
'''
lst=[
    ['01','电风扇','美的',500],
    ['02', '电冰箱', '格力', 500],
    ['03', '电热毯', 'TCL', 500]
]
print('编号\t\t名称\t\t品牌\t\t价格')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()
print('编号\t\t名称\t\t品牌\t\t价格')
for item in lst:
    item[0]='00'+item[0]
    item[3]='${0:.2f}'.format(item[3])
    for i in item:
        print(i,end="\t")
    print()
'''
'''
try:
    score=eval(input("请输入你的成绩"))
    if score<0 or score>100:
        raise Exception('分数不正确')
    else:
        print(f"你的分数是{score}")
except Exception as e:
    print(e)
'''
'''
try:
    a=eval(input("请输入三角形的三边长"))
    b=eval(input("请输入三角形的三边长"))
    c=eval(input("请输入三角形的三边长"))
    if a+b>c and b+c>a and a+c>b:
        print(f'{a}{b}{c}可以成三角形')
    else:
        raise Exception(f'{a}{b}{c}不可以成三角形')
except Exception as e:
    print(e)

'''
'''
lst=[ random.randint(a=1,b=100) for item in range(10)]
lst=[random.randint(1,100) for item in range(10)]

def get_sum(x):
    s=0
    lst=[]
    for item in x:
        if item.isdigit():
            lst.append(int(item))
    s=sum(lst)
    return s,lst

# x=input("请输入一个字符串")
# sum,lst=get_sum(x)
# print(sum,lst)

def lower_upper(x):
    lst=[]
    for item in x:
        if 'A'<=item<='Z':
           lst.append(chr(ord(item)+32))
        elif 'a'<=item<='z':
            lst.append(chr(ord(item)-32))
        else:
            lst.append(item)
    return ''.join(lst)

x=input("请输入要转换的字符串")
print(lower_upper(x))
'''
'''
class Circle():
    def __init__(self,r):
        self.r=r
    def get_area(self):
        s=self.r.__pow__(2)*3.14
        print("圆的面积是:",s)
    def get_perimeter(self):
        c = 2 * 3.14 * self.r
        print("圆的周长:",c)

cir=Circle(3)
cir.get_area()
cir.get_perimeter()
'''

class Student():
    def __init__(self,name,age,score,sex):
        self.name=name
        self.age=age
        self.score=score
        self.sex
    def info(self):
        print(self.name,"  ",self.age,"  ",self.score,"  ",self.sex)



tup=()
for i in range(1,6):
    s=input(f"请输入第{i}位学生的信息 姓名#年龄#分数#性别")
    lst=s.split("#")
    stu=Student(lst[0],lst[1],lst[2],lst[3])
    tup.append(stu)

for i in range(tup):
    print(i.info())





