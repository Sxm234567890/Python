import  threading
from threading import Thread
import time
class SubThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(f'线程：{threading.current_thread().name}正在执行{i}')

if __name__=='__main__':
    print('主线程开始执行')
    Start=time.time()
    lst=[ SubThread() for i in range(2)]
    for item in lst:
        item.start()
    for item in lst:
        item.join()
    print('主线程结束')
    print(f'两个线程一共耗时：{time.time()-Start}')
