def solution(msg):
    answer = []
    dt = {}
    new = 27

    for i in range(1, new):
        a = 64 + i
        dt[chr(a)] = i

    c1, c2 = 0, 0
    while True:
        c2 += 1
        if c2 == len(msg):
            answer.append(dt[msg[c1:c2]])
            break

        if msg[c1:c2 + 1] not in dt.keys():
            dt[msg[c1:c2 + 1]] = new
            new += 1
            answer.append(dt[msg[c1:c2]])
            c1 = c2

    return answer