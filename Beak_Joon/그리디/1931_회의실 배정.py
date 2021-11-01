n = int(input())
data = []

for _ in range(n):
    t1, t2 = map(int, input().split())
    data.append((t1, t2))

data = sorted(data,key=lambda x: (x[1], x[0]))

start = data[0][1]
cnt = 1

for i in range(1, n):
    if start <= data[i][0]:
        start = data[i][1]
        cnt += 1

print(cnt)