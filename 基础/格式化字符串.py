#占位符格式化
name="宋小敏"
age=18
score=99.5
print("姓名：%s，年龄：%d，分数：%f"% (name,age,score))

print("姓名：%s,年龄：%d,分数：%0.3f"%(name,age,score))
print(f"姓名:{name},年龄:{age},分数:{score}")
print("姓名：{0},年龄:{1},分数:{2}".format(name,age,score))#前面的0，1，2是后面的format的索引


s="helloworld"
print('{0:*>20}'.format(s))  #左对齐，占20个位置 空格使用*填充 右填充
print('{0:*<20}'.format(s))
print('{0:*^20}'.format(s))
print('{0: >20}'.format(s))
print(s.center(20,'*'))


print("name:%s,age:%d,score:%0.3f"%(name,age,score))
print("name:{0},age:{1},score:{2}".format(name,age,score))
print("{0: ^20}".format(s))

print('{0:,}'.format(987654321))  #千位分隔符
print('{0:.2f}'.format(3.12343324))
print('保留前：{0:.5}'.format('helloadeaeafaw'))

a=123
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x}'.format(a))
k=10223.345
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(k))

#字符串的编码和解码
s="伟大的中国梦"
scode=s.encode(errors='replace') #默认是utf8,utf8中中文占3个字节
print(scode)
scode_gbk=s.encode('gbk',errors='replace') #gbk中文占2个字节
print(scode_gbk)

#编码中的出错问题
s2='耶✌'
scode_gbk1=s2.encode('gbk',errors='ignore')
print(scode_gbk1)
#scode_gbk2=s2.encode('gbk',errors='strict')  #✌没有对应的编码，replace转换的时候会换成？ ignore会忽略，strict会报错
#print(scode_gbk2)

#解码
print(bytes.decode(scode_gbk1,'gbk'))
print(bytes.decode(scode))