qsize=int(input())
s=[]
command=list(map(str,input().split()))
values=list(map(str,input().split()))
for i in range(len(command)):
    if command[i]=='add':
        if len(s)<qsize:
            s.append(values[i])
        else:
            print('quue is full')
    elif command[i]=='pop':
        s.pop()
    elif command[i]=='size':
        print(len(s))
    elif command[i]=='print':
        for j in range(len(s)):
            
            print(s[len(s)-1-j])