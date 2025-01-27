def is_prime_digit(digit):
    return digit in '2357'

def process_number(num_str):
    result = []
    current_segment = []
    
    for digit in num_str:
        current_segment.append(digit)
        if is_prime_digit(digit):
            # Reverse the current segment (excluding the prime digit)
            result.append(''.join(reversed(current_segment[:-1])))
            # Add the prime digit itself
            result.append(digit)
            # Reset current segment
            current_segment = []
    
    # Add remaining digits (if any)
    result.append(''.join(reversed(current_segment)))
    
    return ''.join(result)
n=int(input())
out=[]
for _ in range(n):
    a=int(input())
    s=input()
    out.append(process_number(s))
for i in out:
    print(i)
