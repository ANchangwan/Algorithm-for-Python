from itertools import combinations

def find(candidate):
    keys = []
    idx = [i for i in range(len(candidate))]
    for k in range(2, len(candidate)+1):
        for li in combinations(idx, k):
            res = list(zip(*(candidate[i] for i in li)))
            if len(set(res)) != len(res):
                continue
            for key in keys:
                if set(key).issubset(li):
                    break
            else:
                keys.append(set(li))
    return len(keys)

def solution(relation):
    answer = 0
    reverse = list(zip(*relation))
    candidate = []
    for col in reverse:
        if len(set(col)) == len(col):
            answer += 1
        else:
            candidate.append(col)
    answer += find(candidate)
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))