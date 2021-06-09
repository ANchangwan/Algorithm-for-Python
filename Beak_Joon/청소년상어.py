import copy

lst = [[None]*4 for _ in range(4)]

for i in range(4):
    fish = list(map(int,input().split()))
    for j in range(4):
        lst[i][j] = [fish[j*2], fish[j*2+1] -1]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def turn_left(dir):
    return (dir + 1) % 8

result = 0

def search_fish(lst, index):
    for i in range(4):
        for j in range(4):
            if lst[i][j][0] == index:
                return (i, j)
    return None

def move_all_fishes(lst,now_x, now_y):
    for i in range(1,17):
        position = search_fish(lst, i)
        if position != None:
            x, y = position[0], position[1]
            dir = lst[x][y][1]
            for j in range(8):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        lst[x][y][1] = dir
                        lst[x][y], lst[nx][ny] = lst[nx][ny], lst[x][y]
                        break
                dir = turn_left(dir)

def get_possible_positions(lst, now_x, now_y):
    positions = []
    dir = lst[now_x][now_y][1]

    for i in range(4):
        now_x += dx[dir]
        now_y += dy[dir]

        if 0 <= now_x and now_x <4 and 0 <= now_y and now_y < 4:
            if lst[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

def dfs(lst, now_x, now_y, total):
    global result
    lst = copy.deepcopy(lst)

    total += lst[now_x][now_y][0]
    lst[now_x][now_y][0] = -1

    move_all_fishes(lst,now_x,now_y)

    positions = get_possible_positions(lst, now_x,now_y)

    if len(positions) ==0 :
        result = max(result, total)
        return
    for next_x, next_y in positions:
        dfs(lst, next_x, next_y, total)


dfs(lst,0,0,0)
print(result)