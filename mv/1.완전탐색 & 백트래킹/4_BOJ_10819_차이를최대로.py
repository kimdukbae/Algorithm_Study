'''
# 1. 순열 (제일 먼저 생각한 풀이 방법)
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
answer = 0

for nPr in permutations(A, N):
    mid_sum = 0
    for i in range(len(nPr) - 1):
        mid_sum += abs(nPr[i] - nPr[i + 1])

    if mid_sum > answer:
        answer = mid_sum

print(answer)
'''

# 2. 백트래킹
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

visited, explore = [0] * N, []
result = []


# 순열(permutations)을 재귀함수로 구현했다고 생각하면 됨.
def backtracking(depth):
    if depth == N:
        result.append(sum(abs(explore[i] - explore[i + 1]) for i in range(N - 1)))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            explore.append(A[i])
            backtracking(depth + 1)
            visited[i] = 0
            explore.pop()


backtracking(0)
print(max(result))
