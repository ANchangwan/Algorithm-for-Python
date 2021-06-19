def solution(A):
    result = []
    for i, v in enumerate(A):
        result.append((i - v, -1))
        result.append((i + v, 1))

    result.sort()
    intersection = 0
    intervals = 0
    for i, v in enumerate(result):
        if v[1] == 1:
            intervals -= 1
        if v[1] == -1:
            intersection += intervals
            intervals += 1

    if intersection > 10000000:
        return -1

    return intersection
