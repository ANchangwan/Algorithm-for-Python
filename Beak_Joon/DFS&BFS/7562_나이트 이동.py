from collections import deque

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

def bfs(start_x,start_y,end_x,end_y):
    q = deque()
    q.append((start_x,start_y))
    graph[start_x][start_y] = 1
    while q:
        x,y = q.popleft()
        if end_x == x and end_y == y:
            return graph[end_x][end_y] - 1
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx >=0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
for _ in range(int(input())):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    start_x,start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    graph[end_x][end_y] = -1

    print(bfs(start_x,start_y,end_x,end_y))






