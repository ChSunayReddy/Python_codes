'''txt file
ob.read()------>read the content in the file
ob.readline()
ob.readlines()------->prints as list'''
#ob=open("text.txt","r")
'''op1=ob.read()
op2=ob.readline()'''
#op3=ob.readlines()
#print(op3)


'''file=open("text.txt",'a')
data=[
    "line 1\n",
    "line 2\n",
    "line 3\n",
    "line 4\n",
    "line 5\n",
    ]
file.writelines(data)      #for single line just file.write()
file.close()'''
#json file writing
'''import json
file=open("file1.json",'w')
data={
    "name":" Chatrapathi Shivaji Maharaj",
    "city":"maharashtra"
    }
json.dump(data,file,indent=4)
file.close()'''
#csv file reader
'''import csv
file=open("sample.csv","r")
readerobject=csv.reader(file)       #predefined reader object
print(readerobject)
for i in readerobject:
    print(i)
file.close()'''
#csv file writer
import csv
file =open("sample.csv","w")
writerObj=csv.writer(file)
header=["name","roll no","class"]
body=[
    ["sun","420","rocking"],
    ["mon","111","sudda poosa"]
    ]
writerObj.writerow(header)
writerObj.writerows(body)
file.close()
