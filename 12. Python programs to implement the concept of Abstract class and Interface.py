#12. Python programs to implement the concept of Abstract class and Interface.

from abc import ABC, abstractmethod
class R(ABC):
    def rk(self):
        print("Abstract Base Class")
class K(R):
    def rk(self):
        super().rk()
        print("subclass ")
r = K()
r.rk()

import zope.interface
class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute("foo")
    def method1(self, x):
        pass
    def method2(self):
        pass
print(type(MyInterface))
print(MyInterface.__module__)
print(MyInterface.__name__)
x = MyInterface['x']
print(x)
print(type(x))
