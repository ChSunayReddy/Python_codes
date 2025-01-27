'''class student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(f"My id is {self.id} and my name is {self.name}")
s=student(1,"venu")
s1=student(2,"varshith")
s2=student(3,"vivek")
s3=student(4,"veerender")
s.display()
s1.display()
s2.display()
s3.display()'''
class vehicle:
    def __init__(self,cost,bike):
        self.cost=cost
        self.bike=bike
    def display(self):
        print(f"My bike is {self.bike} and it's cost is {self.cost}")
s=vehicle('1,00,000',"CB Shine")
s1=vehicle('1,00,00,000',"Ducati superleggera V4")
s.display()
s1.display()
