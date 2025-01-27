r,w=map(int,input().split())
m=[]
for i in range(r):
    k=list(map(int,input().split()))
    m.append(k)
l=[]
for i in range(len(m)):
    for j in range(len(m)):
        if i%2==0:
            l.append(m[i][j])
        elif i%2==1:
            l.append(m[i][len(m)-1-j])
    
print(*l)
