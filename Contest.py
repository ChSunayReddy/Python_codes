n=int(input())
k=[]
for _ in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    l=[]
    c=sorted(b)
    for i in range(a):
        if i!=a-1:
            m1=b.index(c[i])
            m2=b.index(c[i+1])
            l.append(abs(m1-m2))
    k.append(sum(b)+sum(l))
for i in k:
    print(i)
