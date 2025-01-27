import csv
class Student:
    def __init__(self,roll):
        self.roll=roll
        file=open("sample.csv","r")
        self.dbreader=csv.reader(file)
    def getdetails(self,roll):
        def search(ele):
            if ele[2]==roll:
                return ele
        data=list(self.dbreader)
        mydata=list(filter(search,data))
        return mydata[0]
    def displaydetails(self):
        data=self.getdetails(self.roll)
        print(data)
s1=Student("420")
s1.displaydetails()
class Faculty(Student):
    def __init__(self):
        file=open("sample.csv","r")
        self.dbreader=csv.reader(file)
    def addstudent(self):
        pass
    def updatestudent(self):
        pass
fac=Faculty()
res=fac.getdetails("111")
