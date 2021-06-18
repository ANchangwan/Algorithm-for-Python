def solution(A):
    move_east = 1
    passing_car = 0

    try:
        east_idx = A.index(0)
    except:
        return 0

    for i in range(east_idx + 1, len(A)):

        if A[i] == 1:
            passing_car += move_east

            if passing_car > 1000000000:
                return -1
        else:
            move_east += 1

    return passing_car