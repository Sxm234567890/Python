class Person():
   school='北京大学'   #类属性
   def __init__(self,xm,age):
      self.name=xm     #将xm局部变量的值赋值给self.name    实例属性
      self.age=age

   def show(self):
        print(f"我叫{self.name},我今年{self.age}岁")
#静态方法
   @staticmethod
   def sm():
       print("在静态方法中。不能使用实例属性，也不能调用实例方法")
   @classmethod
   def cm(cls):
       print("在类方法中，不能调用实例属性和实例方法")


class Cat():
    pass

class Dog:
    pass

#类方法 静态方法 类属性都是类调用
stu=Person(xm='xmin',age=18)
print(stu.name,stu.age)
print(Person.school)   #类属性
stu.show()             #实例方法
Person.cm()
Person.sm()


c=Cat()
print(type(c))