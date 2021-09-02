from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        orders_all = []
        for order in orders:
            for li in combinations(order, c):
                res = "".join(sorted(li))
                orders_all.append(res)
        new_course = Counter(orders_all).most_common()
        answer += [menu for menu, cnt in new_course if cnt > 1 and cnt == new_course[0][1]]
    return sorted(answer)
