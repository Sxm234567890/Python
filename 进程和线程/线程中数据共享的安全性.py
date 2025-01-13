import threading
from threading import Thread,Lock
import time
ticket=50
Locker1=Lock()
def sale_ticket():
    global ticket
    for i in range(100):
        Locker1.acquire()#上锁
        if ticket>0:
            print(f'当前线程{threading.current_thread().name}在执行{ticket}')
            ticket-=1
        Locker1.release() #解锁
        time.sleep(1)
if __name__=='__main__':
    for i in range(3):
        t=Thread(target=sale_ticket)
        t.start()
        #t.join()