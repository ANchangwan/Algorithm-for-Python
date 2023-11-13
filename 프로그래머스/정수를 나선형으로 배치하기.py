def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y,direction = 0,0, 0
    for num in range(1, n*n+1):
        answer[x][y] = num
        nx,ny = x+dx[direction], y+dy[direction]
        if 0 <= nx < n and 0 <= ny < n and answer[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction = (direction + 1) % 4
            x, y = x + dx[direction], y + dy[direction]
              
    return answer
