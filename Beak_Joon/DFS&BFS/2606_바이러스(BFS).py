# BFS
from collections import deque
n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

cnt = 0

def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                q.append(i)

bfs(1)

print(cnt)