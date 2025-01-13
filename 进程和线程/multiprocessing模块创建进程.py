# from multiprocessing import Process
# import os,time
# def sub_process(name):
#     print(f'子进程的PID:{os.getpid()},父进程的PID:{os.getppid()},----{name}')
#     time.sleep(10)
#     print('i love dami ')
# def sub_process1():
#     print(f'子进程的PID:{os.getpid()}')
#     time.sleep(1)
#
# lst=[]
# if __name__=='__main__':
#     print('主进程开始执行')
#     for i in range(5):
#         p=Process(target=sub_process(i))
#         p1=Process(target=sub_process1())
#         p.start()
#         p1.start()
#         #启动中的进程添加到列表中
#         lst.append(p)
#         #p.join()
#         print('主进程执行结束')

from multiprocessing import  Process
import os,time
def sub_process(name):
    print(f'子进程的pid为:{os.getpid()},父进程的pid为：{os.getppid()}----{name}')
    time.sleep(1)
def sub_process1(name):
    print(f'子进程的pid为：{os.getpid()}')
    time.sleep(10)
if __name__=='__main__':
    for i in range(5):
        p=Process(target=sub_process,args=('dami',))
        p1=Process(target=sub_process1,args=(18,))
        p1.start()
        p.start()
        print(p.name,'是否执行结束',p.is_alive())
        p.join()
        print(p1.name,'是否执行结束',p1.is_alive())
    print('父进程执行完毕')























