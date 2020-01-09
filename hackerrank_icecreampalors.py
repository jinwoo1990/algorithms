import sys

sys.stdin = open("input.txt", "rt")
#sys.stdin = open("input2.txt", "rt")

input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    m = int(input())
    n = int(input())
    cost = list(map(int, input().split()))
    memo = {}
    for i, c in enumerate(cost):
        #print(i, c)
        if (m - c) in memo:
            print("m", m)
            print("c", c)
            print("m-c", m-c)
            print('%s %s' % (memo[m - c], i + 1))
            break
        memo[c] = i + 1
        print("memo", memo)
