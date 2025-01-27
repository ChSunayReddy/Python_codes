def duplicate_nums(n):
    duplicate=set()
    for i in n:
        if i in duplicate:
            return True
        duplicate.add(i)
    return False
n=list(map(int,input().split()))
print(duplicate_nums(n))