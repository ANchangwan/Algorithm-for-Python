from collections import deque
INF = 1e9

# 맵의 크기 입력
n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 아기 상어의 위치와 크기
babyshark_size = 2
now_x, now_y = 0, 0

# 아기 상어의 현재 크기 변수와 현재 위치 변수
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 모든 위치까지의 '최단 거리만' 계산하는 bfs
def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    dist = [[-1]* n for _ in range(n)]
    # 시작 위치는 도달 가능하다고 보며 가리는 0
    q = deque([(now_x,now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0<=ny and ny < n:
                if dist[nx][ny] == -1 and array[nx][ny] <= babyshark_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    # 모든 위치에 최단 거리 테이블 반환
    return dist

# 최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1<= array[i][j] and array[i][j] < babyshark_size:
                if dist[i][j] < min_dist:
                    x, y = i,j
                    min_dist = dist[i][j]

    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result = 0
ate = 0

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에는 이제 아무것도 없도록 처리
        array[now_x][now_y] = 0
        ate += 1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= babyshark_size:
            babyshark_size += 1
            ate = 0
