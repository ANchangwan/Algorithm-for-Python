from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque([(v, i) for i, v in enumerate(priorities)])

    while q:
        p = q.popleft()
        if len(q) != 0:
            if p[0] < max(q)[0]:
                q.append(p)
            else:
                answer += 1
                if p[1] == location:
                    break
        else:
            answer += 1
            if p[1] == location:
                break
    return answer