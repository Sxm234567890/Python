#多态
'''
class Person:
    def eat(self):
        print("人吃骨头")

class Cat:
    def eat(self):
        print("猫吃鱼")

class Dog:
    def eat(self):
        print("狗吃骨头")

def fun(obj):
    obj.eat()

per=Person()
dog=Dog()
cat=Cat()
fun(per)   #Python中的堕胎，不关心对象的数据类型，只关心对象是否具有同名方法
fun(cat)
fun(cat)
'''

#object
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):   #这个方法是为了描述对象  重写
        print("这是一个人类，具有name和age两个实例属性")

a=Person("dea",10)
a.__str__()










