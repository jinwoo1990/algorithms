#!/bin/python3
# -*- coding: utf-8 -*-

#라이브러리---------------------------------------------------------------------------#
import sys
import math
import random
import re

# 필요한 라이브러리들
# https://9kilometer.github.io/record/python-useful-things-for-algorithm-solve/

# hacckeranks 풀이
#https://leechamin.tistory.com/297

# 힙큐
#import heapq as hq

# 큐, 스택
# import queue
# queue(), put(), get(), size(), empty()
from collections import deque
# appendleft(), append(), popleft(), pop()
'''
q = [(pos, val) for pos, val in enumerate(ar)]
    q = deque(q)
    cnt = 0
    
    while True:
        cur = q.popleft()
        if any(cur[1]<x[1] for x in q):
            q.append(cur)
        else:
            cnt += 1
            if cur[0] == m:
                print(cnt)
                break
    
'''
#BFS
'''
chk = [[0] *7 for _ in range(7)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    #dx= [-1, -1, 0, 1, 1, 1, 0, -1]
    #dy= [0, 1, 1, 1, 0, -1, -1, -1]
    dis = [[0]*7 for _ in range(7)]
    deq = deque()
    deq.append((0,0))
    chk[0][0] = 1
    
    while deq:
        
        now = deq.popleft()
        #print(now)
        if now == (6,6):
            break
        
        for j in range(4):
            x = now[0] + dx[j]
            y = now[1] + dy[j]
            if 0 <= x <= 6 and 0<= y <= 6:
                if chk[x][y] == 0 and ar[x][y] == 0:
                    chk[x][y] += 1
                    dis[x][y] = dis[now[0]][now[1]] + 1
                    deq.append((x,y))
        #res += 1
    
    if dis[6][6]==0:
        return -1
    else: 
        return dis[6][6]
'''    

# 순열, 조합
from itertools import combinations
'''
res = [0]*(n+1)
cnt = 0
comb = []
def DFS(L, s):
    
    global cnt
    
    temp = []
    
    if L == m:
        for j in range(L):
            #print(res[j], end = " ")
            temp.append(res[j])
        cnt += 1    
        #print()
        #print(temp)
        comb.append(temp)
    else:
        for i in range(s, n+1):
            res[L]=i
            DFS(L+1, i+1)
            
    return comb
print(DFS(0,1))'''
'''
res = [0]*(n+1)
cnt = 0
comb = []

def DFS(L, s):
    
    temp = []
    
    if L == k:
        for i in range(k):
            temp.append(res[i])
        comb.append(temp)
    else:
        for j in range(s,n+1):
            res[L] = ar[j-1]
            DFS(L+1, j+1)
    return comb
'''
#c = list(com(range(1, n+1), m))
#for x in c:
#    print(*x)
#from itertools import combinations_with_replacement
#from itertools import permutations
'''
res = [0]*n
ch = [0]*(n+1)
cnt = 0
def DFS(L):
    
    global cnt
    
    if L == m:
        for i in range(m):
            print(res[i],end =" ")
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0
            
        
              
    return

DFS(0)
print(cnt)
'''
#from itertools import product
'''
def DFS(L):
    
    #global cnt
    
    if L == m:
        for j in range(m):
            print(res[j], end= " ")
        print()
        #cnt += 1

    else:
        for i in range(1, n+1):
            res[L] = i
            print(res)
            DFS(L+1)

#DFS(0)
'''

# 그래프 
'''
n = 6 # 노드의 수
m = 9 # 간선의 개수
g[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    b[b][a] = 1
    # g[a][b] = c # 방향 그래프 일 때 
    
for i in range(1, n+1): # 1부터 시작해서 0번 무시하고 출력, 더 안 헷갈릴 듯 
    for j in range(1, n+1):
        print(g[i][j], end = ' ')
    print()
'''

# 해쉬
#from collections import Counter
'''
def Counter_cust(x):
    
    result = {}
    
    for item in list(x):
        result[item] = result.get(item, 0) + 1 

    return result
'''
#Counter가 아닌 Dictionary - 연산 
#https://www.geeksforgeeks.org/python-subtraction-of-dictionaries/
#res = {key: test_dict2[key] - test_dict1.get(key, 0) for key in test_dict2.keys()}

#다이나믹 프로그래밍
'''
dy = [0] * (n+1)
    dy[1] = 1
    dy[2] = 2
    
    print(dy)
    for i in range(2, n+1):
        
        if ar[i-1] > dy[i-1]:
            dy[i] = ar[i-1]    
    
    return dy
    
'''

# 냅색 
'''
def solution(n):
    
    for item in ar:
        w = item[0]
        v = item[1]
        #print(w, v)
        for j in range(w, k+1):
            dy[j] = max(dy[j], dy[j-w]+v)
        
        
    return dy[k]
'''
# 플로이드 와샬
'''
for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][j]+dis[k][j])
'''

sys.stdin = open("input.txt", "rt")
#sys.stdin = open("input2.txt", "rt")

input = lambda: sys.stdin.readline().rstrip()

#함수생성---------------------------------------------------------------------------#
            
def solution(n, s):
    
    cnt = 0
    height = 0 
    temp = []
    
    for item in s:
        #print(item)
        if item == 'U':
            temp.append(1)
            height += 1
            if height == 0:
                cnt += 1
        else:
            temp.append(-1)
            height -= 1
            #if height == 0:
                #cnt += 1
        #print(height)
    #print(temp)
    #DFS(0, 0)
    #DFS(0)
    #DFS(1, 0, 0, 0)
    
    return cnt


if __name__ == "__main__":

    
    #기본입력받기---------------------------------------------------------------------------#

    n = int(input())
    #n, m = list(map(int, input().split()))
    s = input()
    #s = list(map(int, input()))
    ar = []
    g = []
    # 한 줄 입력
    #ar = list(map(int, input().rstrip().split()))
    #ar.sort()
    
    
    # 여러 줄 입력 나올 때
    '''
    for _ in range(n):
        temp = int(input())
        ar.append(temp)
    '''
    '''
    for _ in range(t):
        n, s, e, k = list(map(int, input().split()))
        numbers = list(map(int, input().split()))
        
        ar.append([n,s,e,k,numbers])
    ''' 
    
    '''
    for _ in range(n):
        temp = int(input())
        
        # 문자열일때
        #temp = temp.upper()
        #temp.sort()
        ar.append(temp)
    '''
    # 그래프
    '''
    graph=[[0]*(n+1) for _ in range(n+1)]
    degree=[0]*(n+1)
    dQ=deque()
    for i in range(m):
        a, b=map(int, input().split())
        graph[a][b]=1
        degree[b]+=1
    '''    
    '''
    g = [[0]*(n+1) for i in range(n+1)]
    for j in range(m):
        
        a, b = list(map(int, input().split()))
        g[a][b] = 1
    ''' 
     
    
    #글로벌 변수 선언 ---------------------------------------------------------------------------#
    cnt = 0
    #max_profit = -2147000
    #res = [0]*(n+1)
    n = len(s)
    #s.insert(n,-1)
    #res = [0]*(n+3)
    #chk = [0] * (len(s)+1) # DFS
    #path = [] # 경로찾기
    #path.append(1) # 경로찾기
    #chk[1] = 1 # 1부터 시작할 때
    #s = sum(ar)
    #res = set()
    #min_v = 2147000
    #money = [0]*3
    
    # ** 조심, 필요없으면 지우기 
    #ar.insert(0, 0) # 0번째에 0 넣어서 다이나믹 하기 편하게 
    #dy = [0]*(n+1) # 다이나믹 프로그래밍, 메모이제이션
    
    # 변수 출력
    print()
    print("variable")
    print(n)
    print(s)
    
    #print(n, m)
    #print(n,k)
    # 배열 출력
    print()
    print("array")
    print(ar)
    # 그래프 출력
    print()
    print("graph")
    print(g)
    # 추가 변수 출력
    #print(something)
    print()

    #출력---------------------------------------------------------------------------#
    
    print("")
    print("solution:")
    #print(DFS(n))
    #DFS(0,1)
    #print(result)
    #print(solution(n, k, ar))
    #print(solution(n))
    #print(solution(s))
    #print(solution(n,ar,m))
    #print(solution(n, ar))
    #print(solution(n, m, ar))
    print(solution(n, s))
    #print(cnt)

    #---------------------------------------------------------------------------#
