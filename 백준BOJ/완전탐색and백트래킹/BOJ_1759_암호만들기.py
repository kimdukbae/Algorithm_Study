# 조합
import sys
from itertools import combinations

input = sys.stdin.readline
L, C = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()


def check(string):
    count = 0
    for alpha in string:
        if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u':
            count += 1
    return count


for case in combinations(alphabet, L):
    if check(case) >= 1 and (len(case) - check(case)) >= 2:
        print(''.join(case))


# 백트래킹
# import sys
#
# input = sys.stdin.readline
# L, C = map(int, input().split())
# alphabet = list(input().split())
# alphabet.sort()
# visited = [0] * C
#
#
# def check(string):
#     count = 0
#     for alpha in string:
#         if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u':
#             count += 1
#     return count
#
#
# def dfs(depth, string, idx):
#     if depth == L:
#         if check(string) >= 1 and (len(string) - check(string)) >= 2:
#             print(''.join(string))
#             return
#
#     for i in range(C):
#         if idx < i:
#             if not visited[i]:
#                 visited[i] = 1
#                 string.append(alphabet[i])
#                 dfs(depth + 1, string, i)
#                 visited[i] = 0
#                 string.pop()
#
#
# dfs(0, [], -1)
