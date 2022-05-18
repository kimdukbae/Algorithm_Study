import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    op = input().rstrip()
    explore = [op[0]]

    for i in range(1, len(op)):
        if op[i] == '(':
            explore.append(op[i])
        elif op[i] == ')':
            if len(explore) > 0 and explore[-1] == '(':
                explore.pop()
            else:
                explore.append(op[i])

    if len(explore) <= 0:
        print('YES')
    else:
        print('NO')
