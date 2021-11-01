n, k = map(int, input().split())
coin = []

for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

cnt = 0
for x in coin:
    while True:
        if x <= k:
            k -= x
            cnt += 1
        else:
            break

print(cnt)
