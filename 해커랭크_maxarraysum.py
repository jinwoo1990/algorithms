#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.



def maxSubsetSum(arr):

    dp = [arr[0], max(arr[:2])] +[0]*(len(arr)-2)
    for i in range(2,len(arr)):
        dp[i] = max(arr[i], dp[i-1], dp[i-2]+arr[i])
    return dp[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    max_sum = -2147000
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
