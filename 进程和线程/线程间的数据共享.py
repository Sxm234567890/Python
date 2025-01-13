#线程之间是能够数据共享的
import threading
from threading import Thread
import time
a=100
def add_test():
    global a
    a+=10
    print(f'线程{threading.current_thread().name},a={a}')
    time.sleep(1)
def sub_test():
    global a
    a-=20
    print(f'线程{threading.current_thread().name},a={a}')
if  __name__=='__main__':
    print("主线程开始执行")
    t1=Thread(target=add_test)
    t2=Thread(target=sub_test)
    t1.start()
    t2.start()
    # t1.join()
    # t2.join()
    print("主线程结束执行")