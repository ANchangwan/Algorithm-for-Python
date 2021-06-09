# 1
def solution(array, commands):
    answer = []
    arr = []
    for start, end, position in commands:

        for i in range(start - 1, end):
            arr.append(array[i])

        arr.sort()
        answer.append(arr[position - 1])
        arr = []

    return answer


#2 lambda
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#3
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])

    return answer