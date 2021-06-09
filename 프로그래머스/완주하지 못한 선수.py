# 1
def solution(participant,completion):
    answer = ""
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if answer == "":
        answer = participant[len(completion)]
    return answer

# 2
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for x,y in zip(participant,completion):
        if x != y:
            answer = x
            return answer
    return participant[-1]



# Collections 라이브러리 활용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]



