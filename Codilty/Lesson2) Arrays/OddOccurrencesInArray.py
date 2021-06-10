from collections import Counter

def solution(A):
    arr = Counter(A)
    for i in arr:
        if arr[i]%2 == 1:
            return i
