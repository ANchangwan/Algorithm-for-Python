from collections import deque

result = 0
m, n = map(int, input().split())
graph = []
q = deque([])
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])

dx = [1,0,-1,0]
dy = [0,1,0,-1]


while q:
    x, y = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append([nx,ny])

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))

print(result - 1)




