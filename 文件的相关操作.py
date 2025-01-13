#文件的读写操作
def My_write():
    #打开文件
    file=open('a.txt','w',encoding='utf-8')
    file.write("我爱吃大米")
    file.close()
def My_read():
    file=open('a.txt','r',encoding='utf-8')
    s=file.read()
    print(s,type(s))
    file.close()
if  __name__=='__main__':

    My_read()