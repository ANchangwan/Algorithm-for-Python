# DFS
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

lst = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y):

    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            dfs(nx,ny)
        return True
    return False

result = 0
count = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            result += 1
            lst.append(count)
            count = 0

lst.sort()
print(result)
for i in lst:
    print(i)

# BFS
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])