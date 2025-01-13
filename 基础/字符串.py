s1='HelloWorld'
new_s2=s1.lower()
print(s1,new_s2)
new_s3=s1.upper()
print(s1,new_s3)

e_mail='sxm@123.com'
lst=e_mail.split('@')
print("邮箱名：",lst[0],'邮箱服务器域名:',lst[1])

print(s1.count('o'))
print(s1.index('o')) #跟find效果一样，但是不存在会报错
print(s1.find('o'))  #o在字符串s1中首次出现的位置 如果不存在会返回-1


#判断文件后缀前缀
print(s1.startswith('H'))
print("deme.py".endswith('.py'))

#将字符串中的内容进行替换
s="HelloDamioooooo"
new_s=s.replace('o','你好')
print(new_s)
new_s1=s.replace('o','dami',2)
print(new_s1)

#字符串在指定的宽度范围内
print(s.center(20))
print(s.center(20,'*'))  #20是指定宽度，然后*填充空格

#去掉字符串左右空格
s3='  hello  World  '
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())
s4='dl_hello_ld'
print(s4.strip('dl')) #去掉dl或ld  跟顺序无关
print(s4.lstrip('dl')) #去掉左边的dl或者ld
print(s4.rstrip('dl'))




































