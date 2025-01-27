n=int(input())
for i in range(n):
    a='H'*(2*i+1)
    print(a.center(n*2,' '))
for i in range(n+1):
    b='H'*n
    print(b.center(n*2,' ')+b.center(n*6))
for i in range((n+1)//2):
    print(('H'*n*5).center(n*6))
for i in range(n+1):
    f='H'*n
    print(f.center(n*2)+f.center(n*6))
for i in range(n):
    g='H'*((n-i-1)*2+1)
    print(' '*n*3+g.center(n*4))

# c='H'
# for i in range(n):
#     print((c*(2*i+1)).center(2*n))
# for i in range(n + 1):
#     print((c * n).ljust(n * 2) + (c * n).rjust(n * 2))
# for i in range((n + 1) // 2):
#     print((c * n * 5).center(n * 5))
# for i in range(n + 1):
#     print((c * n).ljust(n * 2) + (c * n).rjust(n * 2))
# for i in range(n):
#     print((c * (n - 2 * i - 1)).center(n * 4))