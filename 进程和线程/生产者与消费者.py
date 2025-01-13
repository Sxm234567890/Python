#如果队列为空会生产者就会被唤醒，队列满了生产者就等待
# from queue import Queue
# from threading import  Thread
# import time
# class Producer(Thread):
#     def __init__(self,mingzi,duilie):
#         Thread.__init__(self,name=mingzi)
#         self.queue=duilie
#     def run(self):
#         for i in range(1,11):
#             print(f'{self.name}将产品{i}放入队列')
#             self.queue.put(i)
#             time.sleep(1)
#         print("生产者完成了所以数据的存放")
#
# class Consumer(Thread):
#     def __init__(self,mingzi,duilie):
#          Thread.__init__(self,name=mingzi)
#          #super().__init__(self,name=mingzi)
#          self.queue=duilie
#     def run(self):
#         for _ in range(10):
#             value=self.queue.get()
#             print(f'消费者线程：{self.name}取出了{value}')
#             time.sleep(1)
#         print('-------消费者完成了所以数据的取出--------')
#
# if __name__=='__main__':
#     Fqueue=Queue(100)
#     p=Producer('Producer',Fqueue)
#     c=Consumer('Consumer',Fqueue)
#     p.start()
#     c.start()
#     p.join()
#     c.join()
#     print('主线程执行结束')

from  queue  import Queue
from  threading import  Thread
import threading
import time
class Produce_test(Thread):
    def __init__(self,name,queue):
        #super.__init__(name)
        Thread.__init__(self,name=name)
        self.queue=queue
    def run(self):
        for i in range(1,9):
            self.queue.put(i)
            print(f'进程{self.name}将{i}放入队列')
        time.sleep(1)
        print('生产者线程执行完毕')

class Consumer_test(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.queue=queue
    def run(self):
        for _ in range(5):
            print(f'{self.name}正在消费{self.queue.get()}')
        time.sleep(1)
        print('消费者线程执行完毕')

if __name__=='__main__':
     print("主线程开始执行")
     q1=Queue()
     P1=Produce_test('生产者',q1)
     C1=Consumer_test('消费者',q1)
     P1.start()
     C1.start()
     P1.join()
     C1.join()
     print('主线程执行完毕')


























