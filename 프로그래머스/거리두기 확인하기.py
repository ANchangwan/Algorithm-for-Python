def solution(places):
    answer = []
    for place in places:
        key = False
        room = []

        for n in place:
            room.append(list(n))

        for i in range(5):
            if key:
                break
            for j in range(5):
                if key:
                    break

                if room[i][j] == "P":
                    if i + 1 < 5:
                        if room[i + 1][j] == "P":
                            key = True
                            break

                        if room[i + 1][j] == "O":
                            if i + 2 < 5:
                                if room[i + 2][j] == "P":
                                    key = True
                                    break

                    if j + 1 < 5:
                        if room[i][j + 1] == "P":
                            key = True
                            break

                        if room[i][j + 1] == "O":
                            if j + 2 < 5:
                                if room[i][j + 2] == "P":
                                    key = True
                                    break

                    if i + 1 < 5 and j + 1 < 5:
                        if room[i + 1][j + 1] == "P" and (room[i][j + 1] == "O" or room[i + 1][j] == "O"):
                            key = True
                            break

                    if i + 1 < 5 and j - 1 >= 0:
                        if room[i + 1][j - 1] == "P" and (room[i + 1][j] == "O" or room[i][j - 1] == "O"):
                            key = True
                            break

        if key:
            answer.append(0)
        else:
            answer.append(1)

    return answer