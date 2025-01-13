def my_read(File):
    file=open(File,'w+',encoding='utf-8')
    file.write('你好啊大米')
    file.seek(0)
    #print(file.read())
    #print(file.read(2))  #2个字符
    #print(file.readline(2)) #一行中的两个字符
    #print(file.readlines(1))
    file.seek(3)   #utf-8中一个字符三个字节
    print(file.read())
    file.close()

if __name__=='__main__':
    my_read('a.txt')