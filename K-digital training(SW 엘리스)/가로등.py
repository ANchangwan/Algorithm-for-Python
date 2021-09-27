def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd(b, c)
    return gcd(b % a, a)

num = list(map(int, input().split()))

d = gcd(num[1], num[len(num)-1])

count = 0
for i in range(1, num[len(num)-1] // d):
    val = d * i
    if val not in num:
        count += 1

print(count)