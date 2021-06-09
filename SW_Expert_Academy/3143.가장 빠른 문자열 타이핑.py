for test_case in range(1, T + 1):
    A, B = input().split()
    cnt = A.count(B)
    rt = len(A) - len(B) * cnt + cnt

    print("#{} {}".format(test_case, rt))