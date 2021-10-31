n = int(input())
d = list(map(int, input().split()))
city = list(map(int, input().split()))

res = 0
m = city[0]
for i in range(n-1):
    if city[i] < m:
        m = city[i]
    res += m * d[i]

print(res)