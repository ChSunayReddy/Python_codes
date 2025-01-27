n=int(input())
l=[]
while n>0:
    a=list(map(int,input().split()))
    b=sum(a)
    l.append(b)
    n-=1
print(max(l))