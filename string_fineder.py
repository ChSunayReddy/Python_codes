import re
'''text="How are you?, my no is: 121435423"
#pattern =re.compile(r"[a-z]")  #small letters
#pattern=re.compile(r"[0-9]")    #numbers
pattern=re.compile(r"\s")    #spaces'''
file=open("text.txt","r")
t=file.read()
pattern=re.compile(r"[#%$^&^(]")
arr=re.finditer(pattern, t)
for row in arr:
    print(row)
