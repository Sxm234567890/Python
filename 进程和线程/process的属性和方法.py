from multiprocessing import Process
import os,time
def sub_process1(name):
    print(f'这是process1,当前的线程pid:{os.getpid()},当前线程的父进程pid是:{os.getppid()}---name')

def sub_process2():
    print(f'这是process2')

if __name__=='__main__':
   print("主进程开始执行")
   for i in range(5):
       p=Process()  #没有给定target参数，调用执行Process类中的run方法
       p1=Process(target=sub_process2())
       p2=Process(target=sub_process1('dami'))
       p1.start()
       p2.start()

       #终止进程
       p1.terminate()
       p2.terminate()
   print("主进程执行结束")











