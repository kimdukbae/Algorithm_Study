# 조합
import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for case in combinations(cards, 3):
    mid_sum = sum(case)
    if mid_sum <= M and mid_sum > result:
        result = mid_sum

print(result)


# 백트래킹 (시간초과 뜸) --> dfs() 함수를 잘못 짯나...
# import sys
#
#
# def dfs(depth):
#     if depth == 3 and sum(explore) <= M:
#         result.append(sum(explore))
#     for i in range(N):
#         if visited[i]:
#             continue
#         explore.append(cards[i])
#         visited[i] = 1
#         dfs(depth + 1)
#         visited[i] = 0
#         explore.pop()
#
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
#
# visited = [0] * N
# result, explore = [], []
# dfs(0)
#
# print(max(result))
