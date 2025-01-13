a=10
b=20
print(dir(a))   #python中一切皆对象
print(a.__add__(b))
print(a.__sub__(b))
print(a.__lt__(b))
print(a.__le__(b))
print(a.__eq__(b))
print(a.__gt__(b))
print(a.__ge__(b))
print(a.__ne__(b))
print(a.__mul__(b))
print(a.__truediv__(b))
print(a.__mod__(b))
print(a.__floordiv__(b))
print(a.__pow__(b))


class T():
    def __init__(self,a,b):
       self.sum=(a.__add__(b))

c=T(1,2)
print(c.sum)