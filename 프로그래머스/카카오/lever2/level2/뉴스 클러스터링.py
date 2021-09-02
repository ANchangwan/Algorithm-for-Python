from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    answer = 0
    str1_arr = []
    str2_arr = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_arr.append(str1[i] + str1[i + 1])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_arr.append(str2[i] + str2[i + 1])

    s1 = Counter(str1_arr)
    s2 = Counter(str2_arr)

    first = list((s1 & s2).elements())
    second = list((s1 | s2).elements())

    try:
        answer = int(len(first) / len(second) * 65536)
    except:
        return 65536

    return answer

print(solution("FRANCE", "french"))