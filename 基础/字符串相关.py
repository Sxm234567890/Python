print('123'.isdigit()) #isdigit只识别阿拉伯数字
print('一'.isdigit())
print('123'.isnumeric)
print('一二三'.isnumeric())

print('hello你好'.isalpha()) #识别字母
print('helloworld'.isalpha())
print('helloworld'.isalnum())

print('helloworld'.islower())
print('helloworld'.isupper())

print('Hello'.istitle()) #首字母是否大写
print('\t'.isspace())

#字符串的拼接
s1='hello'
s2='world'
print(s1+s2)
print(''.join([s1,s2]))
print('*'.join([s1,s2]))

print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))
print("%s%s"%(s1,s2))

#字符串的去重
s="hellowadeaelijed"
s1=''
for i in s:
    if i not in s1:
        s1+=i
print(s1)

s2=''
for i in range(len(s)):
    if s[i] not in s2:
        s2+=s[i]
print(s2)

s3=set(s)  #转换为集合  集合无序，不包含重复元素
lst=list(s3)
print(lst)
lst.sort(key=s.index) #列表按照s的排序去排
print(''.join(lst))













