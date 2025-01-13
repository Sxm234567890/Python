def my_write(s):  #a实现追加而非覆盖
    file=open('b.txt','a',encoding='utf-8')#a是追加
    file.write(s)
    file.write('\n')
    file.close()

def my_read():
    file=open('b.txt','r',encoding='utf-8')
    s=file.read()
    print(s)
    file.close()
if '__name__'=='__main__':
    my_write("我爱吃大米")
    my_write("我爱小米")
    my_read()