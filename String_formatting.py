def _formatted(number):
    # your code goes here
    for i in range(1,number+1):
        w=len(bin(number)[2:])
        dec=str(i).rjust(w)
        octal=(oct(i)[2:]).rjust(w)
        hexa_value=(hex(i)[2:].upper()).rjust(w)
        binary_value=(bin(i)[2:]).rjust(w)
        print(f"{dec} {octal} {hexa_value} {binary_value}")
        

if __name__ == '__main__':
    n = int(input())
    _formatted(n)