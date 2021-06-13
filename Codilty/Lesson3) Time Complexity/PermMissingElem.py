# 1
def solution(A):
    A.sort()
    for i in range(len(A)):
        if i+1 != A[i]:
            return i+1
    else:
        return len(A)+1

# 2
def solution(A):
  return sum(range(len(A)+2)) - sum(A)
