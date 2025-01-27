import re
n=str(input())
let=[i for i in n if n.isalpha()]
num=[int(i) for i in re.findall(r'\d')]