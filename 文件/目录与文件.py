import os
import time
import datetime
# for dirs,dirlst,filelst in os.walk('D:'):
#     print(dirs)
#     print(dirlst)
#     print(filelst)
#     print("__________________")
#os.startfile('calc.exe')
#print(time.localtime())
#os.startfile('python.exe')
# print(os.getcwd())
# print(os.listdir('./'))
#os.mkdir('./dami')
#os.makedirs('./dami1/aa/bb/cc')
#os.rmdir('./dami')
#os.removedirs('./dami1/aa/bb/cc')
# os.chdir("../")
# print(os.getcwd())
#os.remove('a.txt')
#os.rename('aa.txt','cc.txt')
# def time_change(longtime):  #传进来的这个应该是以1997那个标准时间为起始经过的时间    时间戳
#     s=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(longtime))
#     return s
#
# s=os.stat('c.txt')
# print(os.stat('c.txt'))
# s1=time_change(s.st_atime)
# print(s1,type(s1))

import os.path
print(os.path.abspath('b.txt'))
print(os.path.exists('b.txt'))
print(os.path.join('b.txt',r'D\python\pythonCode'))
print(os.path.splitext('b.txt'))
print(os.path.basename(r'D:\python\pythonCode\pythonProject2\文件\with模块的使用.py'))
print(os.dirname(r'"D:\python\pythonCode\pythonProject2\文件\with模块的使用.py"'))
print(os.isfile("dami.txt"))
































