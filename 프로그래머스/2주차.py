def check(result):
    answer = ""
    if result >= 90:
        answer += "A"
    elif 80 <= result < 90:
        answer += "B"
    elif 70 <= result < 80:
        answer += "C"
    elif 50 <= result < 70:
        answer += "D"
    else:
        answer += "F"
    return answer


def solution(scores):
    assignment = len(scores)
    answer = ''
    avg = []
    result = 0
    j = 0
    i = 0
    for i in range(assignment):
        for j in range(assignment):
            avg.append(scores[j][i])
        max_value = max(avg)
        min_value = min(avg)
        if avg[i] == max_value and avg.count(max_value) < 2:
            avg.remove(max_value)
            result = sum(avg) / len(avg)
            answer += check(result)
        elif avg[i] == min_value and avg.count(min_value) < 2:
            avg.remove(min_value)
            result = sum(avg) / len(avg)
            answer += check(result)
        else:
            result = sum(avg) / len(avg)
            answer += check(result)
        avg.clear()

    return answer