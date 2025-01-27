import os
def solve(s):
    f=s.split()
    q=[]
    for i in f:
        p=i.capitalize()
        q.append(p)
    return ' '.join(q)

s = input()

result = solve(s)
print(result)
