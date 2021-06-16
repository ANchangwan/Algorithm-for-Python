def solution(S, P, Q):
    result = []
    for i in range(len(P)):
        left = P[i]
        right = Q[i]
        min_num = 5
        if "A" in S[left:right+1]:
            num = 1
        elif "C" in S[left:right+1]:
            num = 2
        elif "G" in S[left:right+1]:
            num = 3
        elif "T" in S[left:right+1]:
            num = 4
        if min_num > num:
            min_num = num
        result.append(min_num)
    return result