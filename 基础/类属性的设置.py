#属性的设置
class Student():
    def __init__(self,name,sex):
        self.name=name
        self.__sex=sex
#使用@property修改方法，将方法转成属性使用
    @property
    def sex(self):
        return self.__sex  #但是只是这样只能得到值，不能修改值
    @sex.setter
    def sex(self,value):  #加了这个之后就在外部通过sex修改
        if value!='男' and value!='女':
            print("性别修改错误，已自动修改成女")
            self.__sex='女'
        else:
            self.__sex=value


stu=Student("dami",'女')
print(stu.sex)   #stu.sex会执行stu.sex()方法
stu.sex='男'
print(stu.sex)

