n = int(input())
graph = []
teachers = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    graph.append(list(map(str, input().split())))
    for j in range(n):
        if graph[i][j] == "T":
            teachers.append((i,j))

def watch():
    for t in teachers:
        for i in range(4):
            x,y = t
            while 0 <= x < n and 0<= y < n:
                if graph[x][y] == "O":
                    break
                elif graph[x][y] == "S":
                    return False
                x += dx[i]
                y += dy[i]
    return True

find = False

def dfs(count):
    global find
    if count > 3:
        return
    if count == 3:
        if watch():
            find = True
            return
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "X":
                count += 1
                graph[i][j] = "O"
                dfs(count)
                if find:
                    return
                graph[i][j] = "X"
                count -= 1


dfs(0)

if find:
    print("YES")
else:
    print("NO")

