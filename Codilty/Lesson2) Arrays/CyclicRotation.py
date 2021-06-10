def solution(A, K):
    if A.count(0) == len(A):
        return A

    K %= len(A)
    new_arr = [None for _ in range(len(A))]
    for i in range(len(A)):
        new_arr[(i+K)%len(A)] = A[i]
    return new_arr