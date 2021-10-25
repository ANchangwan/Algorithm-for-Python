n = int(input())
stack = []
result = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if stack:
            result.append(stack.pop())
        else:
            result.append(-1)
    elif cmd[0] == "size":
        result.append(len(stack))
    elif cmd[0] == "empty":
        if stack:
            result.append(0)
        else:
            result.append(1)
    elif cmd[0] == "top":
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

    cmd.clear()


for i in range(len(result)):
    print(result[i])