#f=open('intro.txt','r')
#f=open('C:\\Users\\k\\Desktop\\sunay\\intro.txt','r')
#print(f.read())
#with open('intro.txt','r') as file:
	#print(file.read())
#with open('intro1.txt','a') as file:
#	file.write("Hello")	
#with open('intro1.txt','r') as file:
#	print(file.read(5))
'''with open('intro1.txt','r') as file:
	c=file.read()
with open('text.txt','w') as file:
	file.write(c)'''
#WRITING TO CSV FILE
'''import csv
with open('example.csv','w') as file:
	writer=csv.writer(file)
	writer.writerow(['Name','Age','City'])
	writer.writerow(['sun','15','london'])
	writer.writerow(['mon','16','USA'])
	writer.writerow(['ram chandra','80','jainad'])
	writer.writerow(['Sushila','59','Deepaiguda'])
	writer.writerow(['Linganna','61','Margudem'])
	writer.writerow(['Nimmala Mohan reddy','70','Sundaragiri'])'''
#WRITING TO A JSON FILES
import json
data={
	'name':'graphes',
	'color':'green',
        'made in ':'kashmir'
	}
with open('examples.json','w') as file:
	json.dump(data,file)
