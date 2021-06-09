# 1
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

# 2
def solution(n, lost, reserve):
    reserved = set(reserve) - set(lost)
    losted = set(lost) - set(reserve)
    for i in reserved:
        if i - 1 in losted:
            losted.remove(i - 1)
        elif i + 1 in losted:
            losted.remove(i + 1)

    return n - len(losted)