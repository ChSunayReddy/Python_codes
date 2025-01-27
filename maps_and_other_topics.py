#maps ,filter and reduce

#maps

'''def square(n):
    return n*n
data=[1,2,3,4,5]
res=list(map(square,data))
print(res)
temp=square
print(temp(10))'''
'''res=[]
for i in data:
    res.append(square(i))
print(res)'''
'''k=[square(i) for i in  data]
print(k)'''

#filter

'''def verify(age):
    return age>18
data=[23,45,67,90,9,13,12]
res=list(filter(verify,data))       #maps :on every elements iteration,,, filter :only useful data(conditioned data),validate every element
print(res)'''

#reduce tool (function)

'''from functools import reduce
def perform(a,b):
    return a*b
data=[1,2,3,4,5]
res=reduce(perform,data)
print(res)'''
#lamda for above codes

'''data=[49,21,13,41,25]
res=list(filter(lambda age:age>18,data))
print(res)


data=[1,2,3,4,5]
res=list(map(lambda num:num*num,data))
print(res)'''


arr=[
    [2,5,4,2,1],
    [1,2,5,7,3],
    [4,6,2,7,2]
    ]
arr.sort(key=lambda row: row[-1])    #using lambda to sort with the last element of the rows
print(*arr,sep="\n")

