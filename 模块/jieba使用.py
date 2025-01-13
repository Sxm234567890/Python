#对中文进行分词的模块
import jieba
with open('dami.txt','r',encoding='utf-8') as file:
    s=file.read()
print(s)
lst=jieba.lcut(s)
print(lst)

set1=set(lst)  #使用集合对列表去重
d={} #key；词，value:出现次数
for item in set1:
    if len(item)>1: #找到词都放到字典中
        d[item]=0

for i in lst:
    if i in d:
        d[item]=d.get(item)+1
print(d)

new_lst=[]
for item in d:
    lst.append([item,d.get(item)])
print(new_lst)
new_lst.sort(key=lambda x:x[1],reverse=Ture)
print(nwe_lst[0:11])

input()#如果打包成exe文件的时候就家这一行可以看到最后的执行结果


