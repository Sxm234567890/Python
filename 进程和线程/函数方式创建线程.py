import threading
from threading import Thread
import time

def test():
    for i in range(3):
        time.sleep(1)
        print(f'线程：{threading.current_thread().name}正在执行{i}')

if __name__=='__main__':
    start=time.time()
    print('主线程开始执行')
    lst=[Thread(target=test) for i in range(2)]
    for item in lst:
        item.start()
    for item in lst:
        item.join()
    print(f'线程运行的时间为{time.time()-start}')
 #主线程负责执行main中的代码，thread-1线程和thread-2执行三次循环
 #三个线程并发执行 谁执行不一定












