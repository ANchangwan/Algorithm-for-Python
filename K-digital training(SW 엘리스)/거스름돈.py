money = int(input())

coin = [500, 100, 50, 10]

cnt = 0
for c in coin:
    while True:
        money -= c
        if money < 0:
            money += c
            break
        cnt += 1

print(cnt)
