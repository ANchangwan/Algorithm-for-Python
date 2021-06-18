def solution(A):
    min_value = 1e9
    for i in range(len(A) - 1):
        avg = (A[i] + A[i + 1]) / 2
        if min_value > avg:
            result = i
            min_value = avg

    for i in range(len(A) - 2):
        avg = (A[i] + A[i + 1] + A[i + 2]) / 3
        if min_value > avg:
            result = i
            min_value = avg

    return result
