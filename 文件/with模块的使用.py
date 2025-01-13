def write_fun():
    with open('aa.txt','w',encoding='utf-8') as file:
        file.write('2025年北京奥运会欢迎你')

def read_fun():
    with open('aa.txt','r',encoding='utf-8') as file:
         print(file.read())


def copy_fun():
    with open('aa.txt','r',encoding='utf-8') as file1:
        with open('bb.txt','w',encoding='utf-8') as file2:
            file2.write(file1.read())


if __name__=='__main__':
      write_fun()
      read_fun()
      copy_fun()
