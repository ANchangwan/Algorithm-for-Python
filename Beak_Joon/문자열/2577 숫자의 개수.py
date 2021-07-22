result = int(input())
keys = [str(i) for i in range(10)]
values = [0] * 10
num_dict = dict(zip(keys, values))

for _ in range(2):
    result *= int(input())

result = str(result)

for i in range(10):
    num_dict[str(i)] = result.count(str(i))
    print(num_dict[str(i)])