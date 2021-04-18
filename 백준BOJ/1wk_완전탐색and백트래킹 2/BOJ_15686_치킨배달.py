import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = [(x, y) for x in range(N) for y in range(N) if city[x][y] == 2]
house = [(x, y) for x in range(N) for y in range(N) if city[x][y] == 1]
minimum = 1e9

for case in combinations(chicken, M):
    total = 0
    for i in range(len(house)):
        mid_sum = 1e9
        for c in case:
            mid_sum = min(mid_sum, abs(house[i][0] - c[0]) + abs(house[i][1] - c[1]))
        total += mid_sum
    if total < minimum:
        minimum = total

print(minimum)


# 2
# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(N)]
#
# chickens = [(x, y) for x in range(N) for y in range(N) if city[x][y] == 2]
# houses = [(x, y) for x in range(N) for y in range(N) if city[x][y] == 1]
# minimum = 1e9
#
# for case in combinations(chickens, M):
#     total = 0
#     for h in houses:
#         total += min([abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in case])
#         # 이전에 계산한 도시의 치킨거리 최솟값보다 중간 계산중인 도시의 치킨거리값이 크거나 같으면 탐색 종료(시간복잡도 줄이는 조건)
#         if minimum <= total: break
#     if total < minimum:
#         minimum = total
#
# print(minimum)


# 백트래킹 방법
# https://steady-coding.tistory.com/23