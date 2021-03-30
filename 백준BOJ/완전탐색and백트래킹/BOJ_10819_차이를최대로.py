# 순열 (내가 푼 방법)
import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

cases = list(permutations(A))

answer = 0
for case in cases:
    mid_sum = 0
    for i in range(N - 1):
        mid_sum += abs(case[i] - case[i + 1])
    answer = max(mid_sum, answer)

print(answer)


# 백트래킹 (인터넷 참고)
# import sys
#
# def dfs(depth):
#     if depth == N:
#         result.append(sum(abs(explore[i] - explore[i + 1]) for i in range(N - 1)))
#         return
#     for i in range(N):
#         if visited[i]:
#             continue
#         explore.append(A[i])
#         visited[i] = 1
#         dfs(depth + 1)
#         visited[i] = 0
#         explore.pop()
#
# input = sys.stdin.readline
# N = int(input())
# A = list(map(int, input().split()))
#
# visited = [0] * N
# result, explore = [], []
# dfs(0)
# print(max(result))
