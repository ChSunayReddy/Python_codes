n=list(map(int,input().split()))
for i in range(len(n)):
    if n.count(n[i])>len(n)/2:
        print(n[i])
        break