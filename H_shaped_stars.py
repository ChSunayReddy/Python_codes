r,c=map(int,input().split())
# for i in range(a):
#     for j in range(b):
#         if i==a//2 or j==b//2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#         print()            
for i in range(r):
    for j in range(c):
        if j==0 or j==c-1 or (j==r//2 and j>0 and j<c-1):
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
            