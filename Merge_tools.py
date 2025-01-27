def merge_the_tools(string, k):
    # your code goes here
    
    for i in range(0,len(string),k):
        sb=string[i:i+k]
        e=''
        for j in sb:
            if j not in e:
                e+=j
        print(e)
s= input()
y=int(input())
merge_the_tools(s,y)