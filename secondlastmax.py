n = int(input())
arr = list(map(int, input().split()))
ne=max(arr)
a=sorted(arr)
for i in arr:
    if i==ne:
        a.remove(i)
print(max(a))