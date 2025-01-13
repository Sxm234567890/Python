#关键字打印
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

luck_num="songdami"
print(id(luck_num))  #打印内存地址
print(round(0.1+0.2,2))
#round(number,ndigits) ndigits是取的小数位

print(r"北京\n欢迎你\n") #\n本来是换行，现在就会打印\n
print(R"北京欢迎你\t")

s="hellowordl"
print(s[0],s[-10])
print(s[2:7])
print(s[-8:-3])
print(s[0:])

#eval()函数去掉字符串左右的引号
s="3+3.14"
print(s,type(s))
x=eval(s)
print(x,type(x))

print("",19<10) #
print(8>0 and  9>0)

print(4&3) #全1为1
print(4|8) #有1为1
print(4^3) #不同为1
print(~4)

print("*"*40) #打印40个*

score=eval(input("请输入你的成绩"))
if score<0 or score>100:
    print("输入的成绩无效")
elif score>60 and score<80 :
    print("优秀")
else:
    print("棒")




