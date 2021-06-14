#1 enumerate
def solution(X, A):
    leaf = set()
    for idx, val in enumerate(A):
        leaf.add(val)
        if len(leaf) == X:
            return idx
    return -1
#2 연결리스트
def solution(X,A):
    B = [False] * (X+1)
    frog_jump = 0
    for i in range(len(A)):
        if B[A[i]] == False:
            B[A[i]] = True
            while frog_jump < X and B[frog_jump+1] == True:
                frog_jump += 1

            if frog_jump == X:
                return i

    return -1