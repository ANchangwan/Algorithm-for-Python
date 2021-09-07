from itertools import combinations
from collections import defaultdict


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for x in info:
        x = x.split()
        info_keys = x[:-1]
        info_val = int(x[-1])
        for i in range(5):
            for a in combinations(x, i):
                tmp_keys = "".join(a)
                info_dict[tmp_keys].append(info_val)

    for keys in info_dict.keys():
        info_dict[keys].sort()

    for q in query:
        q = q.split(" ")
        query_score = int(q[-1])
        q = q[:-1]
        for i in range(3):
            q.remove("and")
        while "-" in q:
            q.remove("-")

        temp_q = "".join(q)

        if temp_q in info_dict:
            scores = info_dict[temp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)

    return answer