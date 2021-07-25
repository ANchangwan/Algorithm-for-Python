rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}


def solution(lottos, win_nums):
    answer = []
    min_count = 0
    max_count = 0

    for win_num in win_nums:
        if win_num in lottos:
            min_count += 1

    max_count = min_count + lottos.count(0)

    if max_count == 0:
        answer = [6, 6]
        return answer

    answer.append(rank[max_count])

    if min_count <= 1:
        answer.append(6)
    else:
        answer.append(rank[min_count])

    return answer

#2 교집합 
rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}

def solution(lottos, win_nums):
    return [rank[len(set(lottos)&set(win_nums)) + lottos.count(0)],rank[len(set(lottos)&set(win_nums))]]
