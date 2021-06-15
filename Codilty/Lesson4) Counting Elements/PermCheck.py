def solution(A):
    A.sort()
    count = 1
    for x in A:
        if count == x:
            count+=1
        else:
            return 0
    return 1
