r,w=map(int,input().split())
m=[]
for i in range(r):
    k=list(map(int,input().split()))
    m.append(k)
p=1
for row in m:
    for ele in row:
        p=p*ele
print(p)