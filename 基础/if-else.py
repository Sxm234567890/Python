'''answer=input('请问你喝酒了吗')
if answer=="y":
   proof=eval(input("请输入你的酒精含量"))
   if  proof<20:
       print("不构成酒驾")
   elif proof>20 and proof<80:
       print("已构成酒驾")
   else :
       print("已构成醉驾")
else:
    print("你没喝酒可以走了")
'''

'''
user_name=input("请输入用户名")
passwd=input("请输入密码")
if user_name=="songxiaomin" and  passwd=="12345" :
   print("登陆成功")
else:
    print("密码或者用户名错误")

score=input("请输入你的成绩")
match score:
    case 'A':
         print("优秀")
    case 'B':
         print("良好")
    case 'C':
         print("及格")

i=348%100
print(i)
'''
answer=eval(input())
if answer==2:
   print(answer)