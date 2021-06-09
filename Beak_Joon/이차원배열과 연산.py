r,c,k = int(input().split())
map = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        map[i][j] = int(input())


def R_funtion(map:list)->row:
    global map_count

    for j in range(3):
        map_count = map[0].count(map[0][j])


