#一个父类可以有多个子类，一个子类可以有多个父类

#一个父类有多个子类
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("我的名字是",self.name,"我的年纪是",self.age)

class Student(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age)   #调用父类的初始化方法
        self.sex=sex

class Doctor(Person):
    def __init__(self,name,age,department):
       super().__init__(name,age)
       self.department=department

stu=Student("songxiaomin",19,"女")
stu.show()

doctor=Doctor("dami",20,"外科")
doctor.show()
'''

'''
#一个子类有多个父类
class AFather():
    def __init__(self,name):
        self.name=name
    def showA(self):
        print("父类a的调用")

class BFather():
    def __init__(self,age):
        self.age=age
    def showB(self):
        print("父类b的调用")

class Son(AFather,BFather):
    def __init__(self,name,age,sex):
        AFather.__init__(self,name)
        BFather.__init__(self,age)
        self.sex=sex
son=Son("dami",20,"女")
son.showA()
son.showB()
'''

#重写
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("我的名字是",self.name,"我的年纪是",self.age)

class Student(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age)   #调用父类的初始化方法
        self.sex=sex
    def show(self):   #重写父类中的方法
        print("我叫",self.name,"我的性别是",self.sex)

class Doctor(Person):
    def __init__(self,name,age,department):
       super().__init__(name,age)
       self.department=department
    def show(self):     #重写
        super().show()
        print("我所在的科室是",self.department)
stu=Student("songxiaomin",19,"女")
stu.show()

doctor=Doctor("dami",20,"外科")
doctor.show()












