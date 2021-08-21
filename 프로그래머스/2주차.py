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
    while i < assignment:
        while j < len(scores):
            avg.append(scores[j][i])
            j += 1
        a = max(avg)
        b = min(avg)
        if avg[i] == a and avg.count(a) < 2:
            avg.remove(a)
            result = sum(avg) / len(avg)
            answer += check(result)
        elif avg[i] == b and avg.count(b) < 2:
            avg.remove(b)
            result = sum(avg) / len(avg)
            answer += check(result)
        else:
            result = sum(avg) / len(avg)
            answer += check(result)
        avg.clear()
        j = 0
        i += 1

    return answer