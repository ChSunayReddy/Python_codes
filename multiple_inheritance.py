class parent1:
    name ="p1"
    def method1(self):
        print("p1")
class parent2:
    name ="p2"
    def method1(self):
        print("p2")
class child(parent1,parent2):
    pass
ob=child()
ob.method1()
