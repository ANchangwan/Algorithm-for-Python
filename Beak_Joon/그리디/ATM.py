n = int(input())
t = list(map(int, input().split()))

t.sort()
person = 0
result = 0
for x in t:
    person += x
    result += person
print(result)