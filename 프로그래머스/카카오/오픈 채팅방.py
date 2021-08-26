def solution(record):
    answer = []
    lst = []
    dt = dict()

    for i in range(len(record)):
        lst.append(list(record[i].split(" ")))

    for i in range(len(lst)):
        if lst[i][0] == "Enter":
            dt[lst[i][1]] = lst[i][2]
        elif lst[i][0] == "Change":
            del dt[lst[i][1]]
            dt[lst[i][1]] = lst[i][2]

    for i in range(len(lst)):
        if lst[i][0] == "Enter":
            answer.append(f"{dt[lst[i][1]]}님이 들어왔습니다.")
        elif lst[i][0] == "Leave":
            answer.append(f"{dt[lst[i][1]]}님이 나갔습니다.")

    return answer
