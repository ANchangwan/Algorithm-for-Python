# 인접 행렬(Adjacency Matrix)
from collections import deque
import sys
read = sys.stdin.readline

def bfs(v):
  q = deque()
  q.append(v)
  visit_list[v] = 1
  while q:
    v = q.popleft()
    print(v, end = " ")
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visit_list[i] = 1

def dfs(v):
  visit_list2[v] = 1
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      dfs(i)

n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)

# 인접 리스트
# 예시에 결과 값은 동일하게 나오는데 IndexError 발생, 이유는 모르겠음
from collections import deque

v, e, start = map(int, input().split())

graph = [[]  for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(e):
    graph[i].sort()

visited = [False] * (v + 1)
bfs_visted = [False] * (v + 1)

def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    bfs_visted[start] = True
    while q:
        node = q.popleft()
        print(node, end= " ")
        for i in graph[node]:
            if not bfs_visted[i]:
                q.append(i)
                bfs_visted[i] = True

dfs(start)
print()
bfs(start)