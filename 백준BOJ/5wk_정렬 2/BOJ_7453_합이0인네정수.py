# Python3 시간 초과 / PyPy3 통과
import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# A + B 배열과
# C + D 배열로 나누기 -> 시간 복잡도 줄이기 위해 (N^4 -> N^2)
first = defaultdict(int)
for i in range(n):
    for j in range(n):
        A_B = A[i] + B[j]
        first[A_B] += 1

answer = 0
for i in range(n):
    for j in range(n):
        C_D = C[i] + D[j]
        # (A + B) + (C + D) == 0일 때 key값에 대한 value만큼 더해준다.
        # (C + D)의 -1을 곱한값이 first에 있으면 A + B + C + D가 0이다.
        if first.get(-C_D):
            answer += first.get(-C_D)

print(answer)

# 전치시키기!
# import sys

# n = int(sys.stdin.readline())
# nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# nums = list(map(list, zip(*nums)))
# print(nums)
