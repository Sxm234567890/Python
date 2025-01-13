# from multiprocessing import Queue
# if __name__=='__main__':
#     q=Queue(3)
#     print('队列是否为空',q.empty())
#     print('队列是否为满',q.full())
#    # q.put('hello')
#     q.put('python')
#     q.put('dami')
#     q.put('nihao')
#     print('当前队列中消息个数：',q.qsize())
#     print('队列是否为满', q.full())
#     if not q.empty():
#      for i in range(q.qsize()):
#           print(q.get_nowait())
#     print('队列是否为空', q.empty())
#     q.put_nowait('dami')
#     q.put_nowait('nihao')
#     q.put_nowait('hongse')
#     #q.put('dami')   #如果这样程序会一直等待队列空一个位置的时候把dami加到队列
#     #q.put_nowait('dami')  #队列消息满了后不等就要加，程序会报错，队列已经满了
#
#     q.get_nowait()
#     q.get_nowait()
#     q.get_nowait()
#     q.get()   #这样程序会一直等待队列里有消息后读出来然后结束
#     q.get_nowait()  #这样队列没有消息后不等
from multiprocessing import Queue,Process

a=100
def write_msg(q):
    global a
    if not q.full():
        for i in range(6):
            a-=10
            q.put(a)
            print('插入的数据为',a)
def read_msg(q):
    global  a
    while not q.empty():
        print(q.get())

if __name__=='__main__':
    q=Queue()  #Queue里面没数就代表队列没有上限
    p1=Process(target=write_msg(q)) #其实这个地方我有点不懂的就是为啥线程1会先执行完然后再执行线程2
    p2=Process(target=read_msg(q))
    p1.start()
    p2.start()
    p1.join()
    p1.join()
    print("主线程执行完毕")