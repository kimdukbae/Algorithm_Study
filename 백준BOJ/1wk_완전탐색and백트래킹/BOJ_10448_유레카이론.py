import sys

answer = [0] * 1001
triangleNum = []
for i in range(1, 45):
    triangleNum.append(i * (i + 1) // 2)

for one in triangleNum:
    for two in triangleNum:
        for three in triangleNum:
            if one + two + three <= 1000:
                answer[one + two + three] = 1

# print(answer)

input = sys.stdin.readline
T = int(input())
K = []
for _ in range(T):
    K.append(int(input()))

for target in K:
    print(answer[target])
