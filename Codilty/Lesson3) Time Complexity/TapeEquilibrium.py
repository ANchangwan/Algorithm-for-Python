# 1
def solution(A):
    p1 = sum(A)
    p2 = 0
    arr1 = []
    arr2 = []
    result = []
    for i in range(len(A)-1):
        p1 -= A[i]
        p2 += A[i]
        arr1.append(p1) # 역방향
        arr2.append(p2) # 양방향

        result.append(abs(arr1[i] - arr2[i]))
    return min(result)
  
  # 2
  
  def solution(A):
    sum_right = sum(A)
    sum_left = 0
    result = None
    for i in range(len(A)-1):
        sum_right -=A[i]
        sum_left += A[i]
        if result == None:
            result = abs(sum_left - sum_right)
        else:
            result = min(result,abs(sum_right - sum_left))
    
    return result
