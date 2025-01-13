data=eval(input("请输入要匹配的数据"))  #注意这个eval,如果输入字符串要有”“ 例 ”helloworld"
match data:
    case [10,20,30]:
        print("列表")
    case ('hello','dami',90):
        print("元组")
    case {1:"dami",2:"xiaomi"}:
        print("集合")
    case _:
        print('相当于多重if中的else')

d1={'a':10,'b':30}
d2={'c':40,'d':50}
#字典合并
merged_dict=d1|d2
print(merged_dict)


#同步迭代
#集合是无序的
fruits=['apple','orange','pear','grape']
counts=[10,3,4,5]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',10:
            print('10个apple')
        case 'orange',3:
            print('3个orange')
        case 'pear',4:
            print('5个pear')
        case 'grape',5:
            print('5个grape')
















