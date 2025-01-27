n=int(input())
a=[]
if n<4:
    print(n)
while n>1:
    for i in range(2,int(2+n//2)):
        if i==(1+n//2):
            a.append(n)
            n//=n
        if n%i==0:
            a.append(i)
            n//=i
            break
print(a)