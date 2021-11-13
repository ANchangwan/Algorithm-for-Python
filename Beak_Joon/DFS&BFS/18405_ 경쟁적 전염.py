from collections import deque

n,k = map(int, input().split())
graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j],0,i,j))

s,x,y = map(int, input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

virus.sort()
q = deque(virus)

while q:
    v,t,_x,_y = q.popleft()

    if t == s:
        break

    for i in range(4):
        nx = dx[i] + _x
        ny = dy[i] + _y
        if nx  <= 0 or nx >= n or ny <= 0 or ny >= n:
            continue
        if graph[nx][ny] != 0:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = v
            t += 1
            q.append((v, t, nx, ny))

print(graph[x-1][y-1])
