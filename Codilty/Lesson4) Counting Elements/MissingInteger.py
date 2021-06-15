def solution(A):
    arr = list(set(A))
    arr.sort()
    miss = 1
    for i in arr:
        if i == miss:
            miss +=1
    return miss
