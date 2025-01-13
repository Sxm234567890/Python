# import random
# import os
# import os.path
# def creat_file(lst1):
#     lst=['水果','烟酒','粮油','肉蛋','蔬菜']
#     code=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#     for i in range(1,30):
#         if i<10:
#            s='0'+str(i)
#         # elif i<100:
#         #     s='00'+str(i)
#         # elif i<1000:
#         #     s='0'+str(i)
#         else:
#             s=str(i)
#         s=s+'_'+random.choice(lst)
#         str1=''
#         for i in range(9):
#             str1+=random.choice(code)
#         s=s+'_'+str1
#         lst1.append(s)
#
# if __name__=='__main__':
#     lst=[]
#     creat_file(lst)
#     #print(lst)
#     path1='./dami'
#     if os.path.exists(path1)==False:
#         os.mkdir(path1)
#     os.chdir(path1)
#     for item in lst:
#         os.mkdir(item)

# import os
# import os.path
#
# def mk_dir(path,num):
#     os.chdir(path)
#     print(os.getcwd())
#     for i in range(num):
#         os.mkdir(path+'_'+str(i))
#
#
# if __name__=='__main__':
#      path='new_dir'
#      if  not os.path.exists(path):
#          os.mkdir(path)
#      num=eval(input('请输入你要创建的文件数量'))
#      mk_dir(path,num)

# import time
# #time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime(time.time()))
# print(time.time())
# def show_info():
#     print("请选择查看日志或者退出：1.退出 2.查看登陆日志")
#
# def write_info(name):
#     with open('info.txt','a',encoding='utf-8') as file:
#         log_time=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
#         file.write(f'用户{name}在{log_time}登陆\n')
#
# def read_info():
#     with open('info.txt','r',encoding='utf-8') as file:
#          lst=file.readlines()
#     for item in lst:
#          print(str(item))
#
# if __name__=='__main__':
#     #write_info('dami')
#     name=input("请输入登陆姓名")
#     password=int(input("请输入密码"))
#     if name=="admi" and password==1234:
#         print("登陆成功")
#         write_info(name)
#         show_info()
#         num=eval(input())
#         while True:
#             if num==1:
#                 break
#             elif num==2:
#                 read_info()
#                 show_info()
#             else:
#                 print("输入的选择错误，请选择0和1")
#                 show_info()
#             num=eval(input())
#     else :
#         print("登入的用户名或密码错误")


def rebot_reply(problem):

      with open('b.txt','r',encoding='utf-8') as file:
         while True:
             s=file.readline()
             if s=='':
                 break
             lst=s.split('|')
             answer=lst[1]
             if lst[0] in problem:
                 return answer
      return False

if __name__=='__main__':
    problem = input("宁好，请问有什么问题问老子")
    while True:
        if problem=='bye':
            break
        answer1 = rebot_reply(problem)
        if answer1!=False:
            print(answer1)
            problem=input("请问还有什么问题,输入bye可以退出")
        else :
            problem= input("你在放什么屁，听不懂,重放，不想放输入bye")































































