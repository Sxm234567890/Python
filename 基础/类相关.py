#动态添加实例的属性和方法
'''
class Student:
    school="考红薯大学"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("展示一下")
stu=Student("xiaomin",18)
stu1=Student("ziwen",20)
stu.gender='女'                   #为实例stu动态添加一个属性
print(stu.name,stu.age,stu.gender)
print(stu1.name,stu1.age)

def example():
    print("为实例添加一个方法")
stu.fun=example   #
stu.show()
stu.fun()
'''

#私有属性，方法和公有属性，方法
class Person():
    def __init__(self,name,age,gender):   #初始化方法
        self._name=name        #self._name 允许本类和子类能访问调用 但是实际上类外部也能访问
        self.__age=age         #self.__age 只能类本身能访问
        self.gender=gender     #都能访问
    def _fun1(self):
        print('子类和本身可以访问')
    def __fun2(self):
        print("只有本身才能访问")
    def show(self):
        self._fun1()
        self.__fun2()
        print(self._name)
        print(self.__age)

stu1=Person("dami",10,'女')
stu1.show()
print(stu1._name)

#这样外部能访问类里的私有属性和方法
print(stu1._Person__age)
stu1._Person__fun2()

print(dir(stu1))   #展示出这个对象的所有对象和方法

#将方法转换为属性




