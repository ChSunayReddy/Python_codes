n1=int(input())
m1=[]
for i in range(n1):
    k=list(map(int,input().split()))
    m1.append(k)
n2=int(input())
m2=[]
for i in range(n2):
    k=list(map(int,input().split()))
    m2.append(k)
add=[[m1[i][j]+m2[i][j] for j in range(n1)]for i in range(n2)]
for i in add:
    print(*i)


