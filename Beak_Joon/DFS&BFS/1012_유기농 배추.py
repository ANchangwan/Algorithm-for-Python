t = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]



def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            dfs(nx,ny)
        return True
    return False

res = []
for _ in range(t):

    n,m,c = map(int,input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(c):
        x, y = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                cnt += 1

    res.append(cnt)

for x in res:
    print(x)


