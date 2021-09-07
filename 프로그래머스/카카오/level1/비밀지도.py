# 1
# 두개 배열을 묶어서 for 문으로 하나씩 꺼내서 쓰고 싶을 때 zip 쓰기
def solution(n, arr1, arr2):
    answer = []
    for ar1, ar2 in zip(arr1, arr2):
        password = bin(ar1 | ar2)[2:]

        if len(password) < n:
            password = "0"*(n - len(password)) + password
        password = password.replace("1", "#")
        password = password.replace("0", " ")
        answer.append(password)
    return answer

# 2

def solution(n, arr1, arr2):
    answer = []
    for ar1, ar2 in zip(arr1, arr2):
        password = bin(ar1 | ar2)[2:]
        password = password.rjust(n, "0")
        password = password.replace("1", "#")
        password = password.replace("0", " ")
        answer.append(password)
    return answer

