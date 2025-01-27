import time

starttime=time.time()
n=list(map(int,input().split()))
m=0
for i in n:
    m=(m*10)+i
m+=1
l=[]
while m>0:
    l.insert(0,m%10)
    m//=10
print(l)

# for i in range(0,10000):
#     print()
endtime=time.time()
runtime=endtime-starttime
print(f"The runtime of the program is : {runtime} seconds or {runtime/1000} milliseconds")