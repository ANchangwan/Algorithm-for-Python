#1
from collections import Counter
def solution(s):
    answer = []
    new = []

    for st in s.split(","):
        new.append(st.strip("{}"))

    arr = Counter(new).most_common()

    for x in arr:
        answer.append(int(x[0]))

    return answer

#2
from collections import Counter
def solution(s):
    new = [st.strip("{}") for st in s.split(",")]
    arr = Counter(new).most_common()
    answer = [int(x[0]) for x in arr]
    return answer