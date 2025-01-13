from multiprocessing import Process
import os,time
#自定义一个类，重写Process中的run方法
class SubProcess(Process):
    def __init__(self,name):
        super().__init__()  #调用父类的初始化方法
        self.name=name
    #改写父类中的run函数
    def run(self):
        print(f'子进程的名字{self.name},pid为{os.getpid()},ppid为{os.getppid()}')
if __name__=='__main__':
    print("主线程开始执行")
    lst=[]
    for i  in range(5):
     p1=SubProcess(f'进程{i}')
     p1.start()
     lst.append(p1)
    for item in lst:
      item.join()
    print('主进程运行完毕')
