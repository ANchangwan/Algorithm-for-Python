from itertools import permutations as pt

def is_prime_number(x):
    x = int(x)
    if x == 1 or x == 0:
      return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = str(numbers)
    lst = []
    for i in range(1, len(numbers)+2):
        temp = list(pt(numbers, i))
        lst = ["".join(p) for p in temp ]
        for x in lst:
            print(x)
            x = x.lstrip("0")
            if is_prime_number(x):
                answer += 1
  
    return answer

print(solution("011"))
