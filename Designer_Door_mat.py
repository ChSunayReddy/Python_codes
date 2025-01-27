a,b=map(int,input().split())
l='.|.'
ad='WELCOME'
if a%2!=0 and b==a*3:
    for i in range(a//2):
        m=l*(2*i+1)
        print(m.center(b,'-'))
    print(ad.center(b,'-'))
    for i in range(a//2-1,-1,-1):
        n=l*(2*i+1)
        print(n.center(b,'-'))

else:
    print("Door mat cannot be created with these inputs")