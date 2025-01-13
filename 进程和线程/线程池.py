from multiprocessing import Pool
import os,time
def test(name):
    print(f'当前运行{os.getpid()}')
    time.sleep(1)
if __name__=='__main__':
    print('父进程开始执行')
    start=time.time()
    print(start)
    lst=[]
    p=Pool(3)
    for i in range(3):
        #非阻塞的状态
        # p.apply_async(func=test,args=(i,))
        #阻塞的方式
        p.apply(func=test, args=(i,))

    p.close()
    p.join()
    print('所以子进程执行完毕，父进程执行结束')
    print(time.time()-start)