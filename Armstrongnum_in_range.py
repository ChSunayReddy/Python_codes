N,m=map(int,input().split())
p=[]
for i in range(N,m+1):
    n=i
    r=0
    l=len(str(i))
    for j in range(l):
        rem=int(n%10)
        r+=pow(rem,l)
        n/=10
    if r==i:
        p.append(i)
print(p)