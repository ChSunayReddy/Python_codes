#one object can used as many functions or methods
#method overloading(compile time)----same method name ,same class,different parameters
#method overriding(runtime)------same method and parameters

#method overloading
class parent1:
    def greet(self, name,age):
        print(f"Hi {name}, you are {age} years old")
    def greet(self):
        print("teja")
    def greet(self, name):
        print(f"Hi {name}")
ob=parent1()
ob.greet("sun" )   #only accepts the latest method
                   #because python manages it's own memory(handles it's own memory) ,that's why python calls it's latest method
                   #while writing make memory allocation less as possible,because companies are paying for it's memory allocation
