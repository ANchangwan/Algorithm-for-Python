# 일반적인 코딩
def solution(nums):
    answer = 0
    length = len(nums) // 2
    monster = list(set(nums))

    for x in monster:
        if answer < length:
            answer += 1

    return answer

# min 함수 사용
def solution(nums):
    remove_repeated_monster = len(list(set(nums)))
    monster = len(nums) // 2

    return min(remove_repeated_monster, monster)

# 조건 표현식
def solution(nums):
    remove_repeated_monster = len(list(set(nums)))
    monster = len(nums) // 2

    return remove_repeated_monster if remove_repeated_monster < monster else monster