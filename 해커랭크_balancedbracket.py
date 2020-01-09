import sys

sys.stdin = open("input.txt", "rt")
#sys.stdin = open("input2.txt", "rt")

input = lambda: sys.stdin.readline().rstrip()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []

    for i, item in enumerate(s):
        if item == "[" or item == "{" or item == "(":
            stack.append(item)
        else:
            if len(stack) == 0:
                return "NO"
            
            if item  == "]":
                stack.append(item)
                if stack[-2] == "[" :
                    stack.pop()
                    stack.pop()
            if item == "}":
                stack.append(item)
                if stack[-2] == "{" :
                    stack.pop()
                    stack.pop()
            if item == ")":
                stack.append(item)
                if stack[-2] == "(" :
                    stack.pop()
                    stack.pop()

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

    return "".join(map(str,stack))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        #print(result)

        fptr.write(result + '\n')

    fptr.close()
