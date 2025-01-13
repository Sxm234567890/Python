def my_copy(src_file,new_file):
    file1=open(src_file,'rb')
    file2=open(new_file,'wb')
    s=file1.read()
    file2.write(s)
    file2.close()
    file1.close()

if __name__=='__main__':
    src='../google.jpg'
    new_file='./goole_c.jpg'
    my_copy(src,new_file)