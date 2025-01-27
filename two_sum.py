n=list(map(int,input().split()))
k=int(input())
l=[]
for i in range(len(n)):
    for j in range(len(n)):
        if i<j:
            if n[i]+n[j]==k:
                l.append((i,j))
print(*l)