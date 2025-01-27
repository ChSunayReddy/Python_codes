#functionality is dispayed ,implementations is hided (login into email)
#only abstract class or interface has abstract methods
'''
1.cannot create objects for abstract classes or interfaces
2.abstract class: class with mixture of abstract and normal methods
3.interface: only has abstract methods
4.we provide methods definitions in the in child class
5.mandatory to provide definitiions for all abstract methods
(doesn't matter if you use them or not '''
from abc import ABC, abstractmethod     #abstract base class
class sample(ABC):

    @abstractmethod             #cannot create objects for abstract classes or interfaces ,because Abstract classes are not complete, as they may have some methods that are not defined
    def method(self):
        print("hello")
ob=sample()
ob.method()    



'''from myPack import Add , Sub

a=int(input())
b=int(input())
Add.perform(2,3)
Sub.perform(3,4)'''
