from prime import prime_list
# prime_list는 1부터 10000사이의 소수가 오름차순으로 저장된 리스트 입니다.

num = list(map(int, input().split()))

check = [False, False] + [True] * 10000

for i in range(2, 101):
    if check[i] == True:
        for j in range(i+i, 10001, i):
            check[j] = False

for n in num:
    A = n // 2
    B = A
    for _ in range(10000):
        if check[A] and check[B]:
            print(A, B)
            break
        A -= 1
        B += 1