def missingCharacters(s):
    l=[0]*123
    result=""
    for i in range(len(s)):
        x=ord(s[i])
        l[x]+=1
    for i in range(48,58):
        if(l[i]==0):
            result+=chr(i)
    for i in range(97,123):
        if(l[i]==0):
            result+=chr(i)
    return result
if __name__ == '__main__':  

    s = input()

    result = missingCharacters(s)