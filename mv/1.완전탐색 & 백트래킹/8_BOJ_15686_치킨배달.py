import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chickens = []
homes = []
for r in range(N):
    for c in range(N):
        if city[r][c] == 2:
            chickens.append((r, c))
        elif city[r][c] == 1:
            homes.append((r, c))

answer = 1e9
for comb in combinations(chickens, M):
    mid_answer = 0
    for home in homes:
        mid_distance = 1e9
        for k in range(len(comb)):
            distance = abs(home[0] - comb[k][0]) + abs(home[1] - comb[k][1])
            if mid_distance > distance:
                mid_distance = distance
        mid_answer += mid_distance

    if answer > mid_answer:
        answer = mid_answer

print(answer)