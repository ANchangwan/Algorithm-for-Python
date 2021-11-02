import heapq
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
q= []

for i in b:
    heapq.heappush(q, i)

a.sort(reverse=True)

result = 0
while q:
    _b = heapq.heappop(q)
    _a = a.pop(0)
    result += _a*_b

print(result)
