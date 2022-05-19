import sys
import heapq

input = sys.stdin.readline

N = int(input())

problems = []
for _ in range(N):
    problems.append(list(map(int, input().split())))
problems.sort()

explore = []

for problem in problems:
    heapq.heappush(explore, problem[1])
    if problem[0] < len(explore):
        heapq.heappop(explore)

print(sum(explore))
