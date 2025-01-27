from datetime import datetime
s=input()
time=datetime.strptime(s,'%I:%M:%S%p')
print(time.strftime('%H:%M:%S'))