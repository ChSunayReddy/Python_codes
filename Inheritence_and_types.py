#Single and Multiple Inheritance
'''class Parent:        #parent
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        print(f"The addition of {self.a} and {self.b} is : {c}")
class Parent1:               #parent1
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add1(self):
        c=self.a+self.b
        print(f"The addition of {self.a} and {self.b} from Parent1 is : {c}")
class child(Parent,Parent1):      #multiple inheritane
    def multiply(self):
        c=self.a*self.b
        print(f"The multiplication of {self.a} and {self.b} is : {c}")
c=child(19899732,284738787)
c.add()
c.add1()
c.multiply()'''
#Multilevel Inheritance
'''class grandParent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        print(f"The addition of {self.a} and {self.b} is : {c}")
class Parent(grandParent):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add1(self):
        c=self.a+self.b
        print(f"The addition of {self.a} and {self.b}  is : {c}")
class child(Parent):
    def multiply(self):
        c=self.a*self.b
        print(f"The multiplication of {self.a} and {self.b} is : {c}")
c=child(19899732,284738787)
c.add()
c.add1()
c.multiply()'''
#hierarchial Inheritance
class Parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        print(f"The addition of {self.a} and {self.b} is : {c}")
class child1(Parent):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add1(self):
        c=self.a+self.b
        print(f"The addition of {self.a} and {self.b}  is : {c}")
class child2(Parent):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def multiply(self):
        c=self.a*self.b
        print(f"The multiplication of {self.a} and {self.b} is : {c}")
c=child1(3,4)
c1=child2(5,6)
c.add()
c1.add()
c1.multiply()
