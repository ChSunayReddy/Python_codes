def print_rangoli(size):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    # your code goes here
    for i in range(size):
        if i==0:
            print(alphabet[size-1].center(4*size-3,'-'))
        else:
            left='-'.join(alphabet[size-1:size-i-1:-1])
            right='-'.join(alphabet[size-i-1:size])
            r=left+'-'+right
            print(r.center(4*size-3,'-'))
        # print(('e'*(2*i+1)).center(4*n-3,'-'))
    for i in range(size-2,-1,-1):
        if i==0:
            print(alphabet[size-1].center(4*size-3,'-'))
        else:
            left_part='-'.join(alphabet[size-1:size-i-1:-1])
            right_part='-'.join(alphabet[size-i-1:size])
            row=left_part+'-'+right_part
            print(row.center(4*size-3,'-'))
        # print(('e'*((2*i+1))).center(4*n-3,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)