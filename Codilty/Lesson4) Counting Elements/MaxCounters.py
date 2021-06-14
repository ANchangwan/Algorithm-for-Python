def solution(N, A):
    arr = {i:0 for i in range(1,N+1)}
    max_num = 0
    max_sum = 0
    for val in A:
        if val == N+1:
            max_sum += max_num
            arr.clear()
            max_num = 0
        else:
            if arr.get(val) is None:
                arr[val] = 1
            else:
                arr[val] += 1
            max_num = max(max_num,arr[val])
    
    answer = [max_sum] * N
    
    for idx,val in arr.items():
        answer[idx - 1 ] += val

    return answer
