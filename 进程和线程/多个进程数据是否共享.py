#进程之间的数据是没有共享的
from  multiprocessing import Process
import os,time
a=100
def add():
    global  a
    a+=30
    print('子进程加法开始执行',a)

def sub():
    global a
    a-=20
    print('子进程减法开始执行',a)
if __name__=='__main__':
    print('主进程开始执行',a)
    p=Process(add())
    p1=Process(sub())
    p1.start()
    p.start()
    p1.join()
    p.join()
    print('主进程结束')
