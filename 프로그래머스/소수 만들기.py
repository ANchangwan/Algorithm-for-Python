from itertools import combinations


def solution(nums):
    answer = 0
    lst = combinations(nums, 3)
    print(lst)
    for i in lst:
        num = sum(i)
        for j in range(2, num):
            if num % j == 0:
                break
        else:
            answer += 1
    return answer


