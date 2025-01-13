import re
pattern=r'\d\.\d+' #0-9数字出现1次或多次 \. :\暗示.此时不是元字符
s='I study Python 3.11 every day'
match=re.match(pattern,s,re.I)#re.I 忽略大小写
print(match)
s2='3.11Python I study Python every day'
match2=re.match(pattern,s2)
print(match)
print('匹配值的起始位置：',match2.start())
print('匹配值的结束位置：',match2.end())
print('待匹配的字符串：',match2.string)
print('匹配区间的位置元素：',match2.span())
print('匹配的数据：',match2.group())

s1="I study Python 3.11 and Python 2.13 every day "
s2="I study Python 3.11"
str1=re.search(pattern,s1)
print(str1.group())
lst=re.findall(pattern,s1)
print(lst)

pattern1='[?|#]'
s1='https://www.zhihu.com/question/51340399?sort=created#:~:text=%E7%BC%96%E5%8F%B75001-999'
lst=re.split(pattern1,s1)
print(lst)

pattern3='黑客|破解|反爬'
s2="我想当黑客，破解密码，实现反爬"
s3=re.sub(pattern3,'xxx',s2)
print(s3)

pattern=r'\s*@'
s='@dami @宋小敏 @大米'
lst=re.split(pattern,s)
print(s)






