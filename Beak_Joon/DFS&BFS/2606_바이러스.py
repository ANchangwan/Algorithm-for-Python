
c = int(input())
n = int(input())

graph = [[] * c for _ in range(c+1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
visited = [False] * (c+1)

cnt = 0
def dfs(graph, visited, start):
    global cnt
    visited[start] = True
    for x in graph[start]:
        if not visited[x]:
            cnt += 1
            dfs(graph, visited, x)

dfs(graph, visited, 1)
print(visited)
print(cnt)
