'''For example, the square matrix  is shown below:
3
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is |15-17|=2.'''
import math
import os
import random
import re
import sys
def diagonalDifference(arr):
    sum=0
    sum1=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i==j:
                sum+=arr[i][j]
            if j==len(arr[i])-1-i:
                sum1+=arr[i][j]
    if sum>sum1:
        return sum-sum1
    else:
        return sum1-sum
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)