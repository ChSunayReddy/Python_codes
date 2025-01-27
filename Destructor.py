class Dogs:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def __def__(self):
        print("Destructor is called")
    def display(self):
        print(f"My dog name is {self.name} and it's color {self.color}")
s=Dogs("German shepperd","Blackish Brown")
s1=Dogs("Dobberman","Blackish Brown")
del s
s1.display()
#s1.display()
