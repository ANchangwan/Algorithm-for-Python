
N = int(input())
map = [0 for _ in range(N) for __ in range()]
result = 0

def isTrue(x):
    for i in range(1,x):
        if map[x] == map[i] or abs(map[x] - map[i]) == x - i:
            return False
    return True

def dfs(cnt):
    global result
    if cnt > N:
        result += 1
    else:
        for i in range(1, N+1):
            map[cnt] = i
            if isTrue(cnt):
                dfs(cnt + 1)

dfs(1)

print("{}".format(result))