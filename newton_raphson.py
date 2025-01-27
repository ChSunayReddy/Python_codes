def f_x(x):
    fun_ord=len(c)
    fx=0
    dfx=0
    for i in range(fun_ord):
        fx+=c[i]*x**(fun_ord-1-i)
    for i in range(fun_ord-1):
        dfx+=c[i]*(fun_ord-1-i)*x**(fun_ord-2-i)
    return ([round(fx,dec),round(dfx,dec)])
c=list(map(int,input().split()))
a,b=map(int,input().split())
dec=int(input())
prev=(a+b)/2
while True:
    f,df=f_x(prev)
    x=prev-f/df
    nxt=round(x,dec)
    if prev==nxt:
        break
    else:
        prev=nxt
print(nxt)