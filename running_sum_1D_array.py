n=list(map(int,input().split()))
k=0
l=[]
for i in n:
    k=k+i
    l.append(k)
print(*l,sep=', ')