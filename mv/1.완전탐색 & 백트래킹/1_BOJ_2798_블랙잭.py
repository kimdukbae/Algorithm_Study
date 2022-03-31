'''
# 1. DFS (내가 제일 먼저 생각한 방법)
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
visited = [False] * N
result = 0
mid = []


def dfs(depth):
    global result

    if depth == 3:
        if result <= M:
            mid.append(result)
        return

    if result > M:
        return

    for i in range(len(card)):
        if not visited[i]:
            visited[i] = True
            result += card[i]
            dfs(depth + 1)
            result -= card[i]
            visited[i] = False


dfs(0)
print(max(mid))
'''

# 1. 백트래킹(DFS)
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
answer = 0


def backtracking(cards, idx, select):
    global answer

    if len(select) == 3:
        mid_sum = sum(select)
        if mid_sum <= M and mid_sum > answer:
            answer = mid_sum

    else:
        for i in range(idx, len(cards)):
            select.append(cards[i])
            backtracking(cards, i + 1, select)
            # print(select)
            select.pop()


backtracking(card, 0, [])
print(answer)

'''
# 2. 조합
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
answer = 0

for case in combinations(card, 3):
    mid_sum = sum(case)
    if mid_sum <= M and mid_sum > answer:
        answer = sum(case)

print(answer)
'''

'''
# 3. 완전탐색
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
answer = 0

for x in range(N - 2):
    for y in range(x + 1, N - 1):
        for z in range(y + 1, N):
            if card[x] + card[y] + card[z] > M:
                continue
            else:
                if card[x] + card[y] + card[z] > answer:
                    answer = card[x] + card[y] + card[z]

print(answer)
'''
