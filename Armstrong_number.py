num=int(input())
n=num
r=0
rem=0
l=len(str(n))
for i in range(l):
    rem=int(n%10)
    r+=pow(rem,l)
    n/=10
if r==num:
    print("The Number is Armstrong Number")
else:
    print("The Number is not a Armstrong Number")