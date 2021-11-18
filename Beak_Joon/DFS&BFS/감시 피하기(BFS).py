from collections import deque
from itertools import combinations as cb
import copy
n = int(input())
graph = []
teacher = []
wall = []
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == "T":
            teacher.append((i,j))
        if graph[i][j] == "X":
            wall.append((i,j))



dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    q = deque(teacher)

    while q:
        x, y = q.popleft()
        temp = copy.deepcopy(graph)
        for i in range(4):
            _x,_y = x,y
            while True:
                nx = _x + dx[i]
                ny = _y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if temp[nx][ny] == "O":
                        break
                    elif temp[nx][ny] == "S":
                        return False
                    _x,_y = nx, ny
                else:
                    break
    return True

find = False
for data in cb(wall, 3):
    for x,y in data:
        graph[x][y] = "O"

    if bfs():
        find = True
        break

    for x, y in data:
        graph[x][y] = "X"

if find:
    print("YES")
else:
    print("NO")
