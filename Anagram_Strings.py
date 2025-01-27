def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = [0] * 26
    for i in s1:
        count[ord(i) - ord('a')] += 1
    for i in s2:
        count[ord(i) - ord('a')] -= 1
    for i in count:
        if i!=0:
            return False
    
    return True
a=input().lower()
b = input().lower()
print(isAnagram(a, b))
