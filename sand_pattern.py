n=int(input())
for i in range(n):
    a='* '*(n-i)
    print(a.center(n*2))
for i in range(2,n+1):
    b='* '*i
    print(b.center(n*2))