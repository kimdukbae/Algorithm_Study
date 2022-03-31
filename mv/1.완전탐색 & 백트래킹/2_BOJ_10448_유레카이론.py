import sys

input = sys.stdin.readline

T = int(input())
K = []
for i in range(T):
    K.append(int(input().strip()))
answer = [0] * 1001
triangle_num = []

for i in range(1, 45):
    triangle_num.append(i * (i + 1) // 2)

for one in triangle_num:
    for two in triangle_num:
        for three in triangle_num:
            if one + two + three <= 1000:
                answer[one + two + three] = 1

for k in K:
    print(answer[k])
