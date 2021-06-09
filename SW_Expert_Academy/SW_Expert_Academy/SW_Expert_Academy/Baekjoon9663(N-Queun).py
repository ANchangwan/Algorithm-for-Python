import sys
n, result= int(sys.stdin.readline()),0

flag_a,flag_b,flag_c = [False] * n,[False] *(n*2 -1),[False] * (n*2 - 1)

def dfs(i):
    global result
    if i == n:
        result += 1
        return
    for j in range(n):
        if( not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + n - 1]):
            flag_a[j] =flag_b[i + j] = flag_c[i- j + n-1] = True
            dfs(i+1)
            flag_a[j] = flag_b[i+j] = flag_c[i - j + n-1] = False

dfs(0)
print(result)
