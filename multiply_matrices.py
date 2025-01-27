r,w=map(int,input().split())
m=[]
for i in range(r):
    k=list(map(int,input().split()))
    m.append(k)
R,W=map(int,input().split())
n=[]
for i in range(R):
    K=list(map(int,input().split()))
    n.append(K)
result = []
for i in range(len(m)):
    r=[]
    for j in range(len(n[0])):
        sum=0
        for k in range(len(n)):
            sum+=m[i][k]*n[k][j]
        r.append(sum)
    result.append(r)
for i in result:
    print(*i)