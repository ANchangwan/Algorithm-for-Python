def solution(a, b):
    answer = 0
    for i in range(1,len(a)+1):
        answer += (a[i-1]*b[i-1])
    return answer