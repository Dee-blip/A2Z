from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.



def fibo(n):
    first=1
    second=1
    
    if n==first:
        return 1
    if n==second:
        return 1
    else:
        for i in range(3,n+1):
            res=first+second
            first=second
            second=res
    return res



n=int(input())
print(fibo(n))
