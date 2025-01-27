n=int(input())
l=[]
for _ in range(n):
    a,b=map(int,input().split())
    if(a<=b):
        l.append(0)
    else:
        c=a-b
        if (c%4==0):
            l.append(c//4)
        else:
            l.append(c//4+1)
for i in l:
    print(i)