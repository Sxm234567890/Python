# def my_write(s):  #a实现追加而非覆盖
#     file=open('c.txt','a',encoding='utf-8')#a是追加
#     file.write(s)
#     file.write('\n')
#     file.close()
#
# def my_read():
#     file=open('c.txt','r',encoding='utf-8')
#     s=file.read()
#     print(s)
#     file.close()
# if  __name__=='__main__':
#     my_write('我爱吃大米')
#     my_write("我爱小米")
#     my_read()

#向文件添加列表
def my_write_list(file,lst):
    file=open(file,'a',encoding='utf-8')
    file.writelines(lst)
    file.close()

if __name__=='__main__':
    lst=['姓名\t','年龄\t','性别\n','小敏\t','98\t','女']  #不能写int型的数据，只能是字符串类型的
    my_write_list('b.txt',lst)











