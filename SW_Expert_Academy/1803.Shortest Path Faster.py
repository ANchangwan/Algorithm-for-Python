from heapq import heappush, heappop

for test_case in range(int(input())):
    N, M, start, end = map(int, input().split())                # 정점의 개수 N, 간선의 개수 M
    graph = [[] for _ in range(N + 1)]
    distance = [float('inf')] * (N + 1)

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append([v, w])
        graph[v].append([u, w])

    distance[start] = 0

    queue = []
    heappush(queue, [0, start])
    while queue:
        val = heappop(queue)[1]

        for v in graph[val]:
            if distance[val] + v[1] < distance[v[0]]:
                distance[v[0]] = distance[val] + v[1]
                heappush(queue, [distance[val] + v[1], v[0]])

    print("#{}".format(test_case+1), distance[end])
