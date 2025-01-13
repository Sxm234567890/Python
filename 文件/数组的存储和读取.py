import json
#一维数据的存储和读取
def my_write():
    lst=['张三','李四','王五','陈六']
    with open('student.csv','w',encoding='utf-8') as file:
        file.write(','.join(lst))

def my_read():
    with open('student.csv','r',encoding='utf-8')  as file:
        print(file.read().split(','))

#二维数据得存储和读取
def my_write_table():
    lst=[['姓名','年龄','性别'],['宋小敏','19','女'],['宋子雯','89','男']]
    with open('table.csv','w',encoding='utf-8') as file:
        for item in lst:
            file.write((',').join(item))
            file.write('\n')
def my_read_table():
    with open('table.csv','r',encoding='utf-8') as file:
        lst=file.readlines()
        for item in lst:
            print(item[:len(item)-1].split(','))


if __name__=='__main__':
    # my_write()
    # my_read()
    #my_write_table()
    #my_read_table()
    #高维数据
    lst=[{'name':"宋小敏",'age':21,'sex':'女'},{'name':'宋子雯','age':30,'sex':'男'},{'name':'宋会敏','age':21,'sex':'女'}]
    # #ensure_ascii正常显示中文，indent增加数据得缩进
    # s=json.dumps(lst,ensure_ascii=False,indent=4)
    # print(s,type(s))
    # lst1=json.loads(s)
    # print(type(lst1))
    # print(lst1)
    with open('student.txt','w',encoding='utf-8') as file:
         json.dump(lst,file,ensure_ascii=False,indent=4)


    with open('student.txt','r',encoding='utf-8') as file:
         lst2=json.load(file)
         print(type(lst2),lst2)

