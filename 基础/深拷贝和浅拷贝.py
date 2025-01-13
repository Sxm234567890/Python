import copy
class Cpu():
    pass

class Disk():
    pass

class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
cpu=Cpu()
disk=Disk()
com=Computer(cpu,disk)
com1=com
print(com)
print(com1)
print(com.cpu,com.disk)
print(com1.cpu,com1.disk)

#浅拷贝
com2=copy.copy(com)
print(com,'子对象的地址',com.cpu,com.disk)
print(com2,'子对象的地址',com2.cpu,com2.disk)

#深拷贝
com3=copy.deepcopy(com)
print(com,'子对象的地址',com.cpu,com.disk)
print(com3,'子对象的地址',com3.cpu,com3.disk)
