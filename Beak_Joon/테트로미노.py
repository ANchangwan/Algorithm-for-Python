
tetrominos_shape = [([0, 0], [0, 1], [0, 2], [0, 3]),  # ----
              ([0, 0], [1, 0], [2, 0], [3, 0]),
              ([0, 0], [0, 1], [1, 1], [1, 0]),  # ㅁ
              # ㄴ 모양
              ([0, 0], [1, 0], [1, 1], [1, 2]),
              ([0, 0], [0, 1], [1, 0], [2, 0]),
              ([0, 0], [0, 1], [0, 2], [1, 2]),
              ([0, 1], [1, 1], [2, 1], [2, 0]),
              ([0, 0], [0, 1], [1, 1], [2, 1]),
              ([1, 0], [1, 1], [1, 2], [0, 2]),
              ([0, 0], [1, 0], [2, 0], [2, 1]),
              ([0, 0], [1, 0], [0, 1], [0, 2]),
              # 번개모양
              ([0, 0], [1, 0], [1, 1], [2, 1]),
              ([1, 0], [1, 1], [0, 1], [0, 2]),
              ([2, 0], [1, 0], [1, 1], [0, 1]),
              ([0, 0], [0, 1], [1, 1], [1, 2]),
              # ㅜ 모양
              ([0, 0], [0, 1], [1, 1], [0, 2]),
              ([1, 0], [0, 1], [1, 1], [2, 1]),
              ([1, 0], [1, 1], [1, 2], [0, 1]),
              ([0, 0], [1, 0], [1, 1], [2, 0])]

def map_sum(a,b,c):
    result =0
    global N,M
    for dx,dy in c:
        nx = a + dx
        ny = b + dy
        if 0<=nx < N and 0<=ny < M:
            result += map_[nx][ny]
        else:
            return -1
    return result



N,M = map(int,input().split())
map_ = []
Max_= 0

for i in range(N):
    map_value = list(map(int, input().split()))
    map_.append(map_value)

for i in range(N):
    for j in range(M):
        for tetromino in tetrominos_shape:
            Max_ = max(Max_,map_sum(i,j,tetromino))

print(Max_)



