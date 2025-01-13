#集合是无序的
A={10,20,30,40,50}
B={10,20,50,60,70,80}
print(A&B)  #交集
print(A|B)  #并集
print(A-B)  #差集
print(A^B)  #补集

A.add(90)
print(A)
A.remove(90)
print(A)
A.clear()
print(A)

for i in B:
    print(i)

for index,item in  enumerate(s):
    print(index,'--->',item)

s={i for i in range(1,10)}
print(s)

s={i for i in range(1,20) if i%2==1}
print(s)
