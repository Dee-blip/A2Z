from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
    dp = [[False for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1,n+1):
        for j in range(1,k+1):
            dp[i][j] = dp[i-1][j]

            if j>= arr[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]

    return dp[n][k]

# def helper(arr,sum1,tempSum,i,memo):
#     if (i,tempSum) in memo:
#         return memo[(i,tempSum)]

#     if sum1 == tempSum:
#         return True
    
#     if i>= len(arr) or tempSum > sum1:
#         return False
 
#     include = helper(arr,sum1,tempSum+arr[i],i+1,memo)
#     exclude = helper(arr,sum1,tempSum,i+1,memo)

#     memo[(i,tempSum)] = include or exclude

#     return memo[(i,tempSum)]
