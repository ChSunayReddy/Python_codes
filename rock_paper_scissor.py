import random
a=input()
l=a.lower()
t=['rock','paper','scissor']
r=random.choice(t)
if (l=='rock' and r=='rock') or (l=='paper' and r=='paper') or (l=='scissor' and r=='scissor') :
    print("Tie")
elif (l=='rock' and r=='scissor') or (l=='scissor' and r=='paper') or (l=='paper' and r=='rock'):
    print("You win")
elif (l=='scissor' and r=='rock') or (l=='paper' and r=='scissor') or (l=='rock' and r=='paper'):
    print("You lose")
