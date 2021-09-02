from itertools import permutations
def solution(expression):
    operators = ["*", "+", "-"]
    answer = []
    for oper in permutations(operators, 3):
        a = oper[0]
        b = oper[1]
        tmp_list = []
        for i in expression.split(a):
            tmp = [f"({j})" for j in i.split(b)]
            tmp_list.append(f"{b.join(tmp)}")
        answer.append(a.join(tmp_list))
    return answer

print(solution("100-200*300-500+20"))