'''n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(str,input().split())))
# for i in range(len(l)):
#     for m in range(i+1,len(l)+1):
#         for j in range(len(l[i])):
#             for k in range(j+1,len(l[i])+1):
#                 if j<k:
#                     if l[i][j]==l[m][j] and l[i][k]==l[m][k]:
#                         print(l[i][j],l[m][k])
minl=min(len(i) for i in l)
cl=[]
for i in range(minl):
    current_char=l[0][i]
    if all(k[i]==current_char for k in l):
        cl.append(current_char)
    else:
        break
print(''.join(cl))'''
l=[1,2,3,4,1,4]
s=set(l)
f=list(s)
print(*l,sep=' ')
