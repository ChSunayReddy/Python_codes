def minion_game(string):
    # your code goes here
    c=0
    c1=0
    vowels="AEIOU"
    # consonents="BCDFGHJKLMNPQRSTVQWXYZ"
    for i in range(len(string)):
        if string[i] in vowels:
            c+=len(string)-i
        else:
            c1+=len(string)-i
    if c>c1:
        print(f"Kevin {c}")
    elif c1>c:
        print(f"Stuart {c1}")
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)