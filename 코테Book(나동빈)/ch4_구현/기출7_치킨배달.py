# import itertools, sys
#
# N, M = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(N)]
# # city = [[0] * N for _ in range(N)]
#
# # for i in range(N):
# #     city[i] = (list(map(int, input().split())))
#
# chicken = []
# for r in range(N):
#     for c in range(N):
#         if city[r][c] == 2:
#             chicken.append((r, c))
#
# chicken_nCr = list(itertools.combinations(chicken, M))
#
# min_distance = sys.maxsize
# for i in range(len(chicken_nCr)):
#     distance = 0
#     for m in range(N):
#         for n in range(N):
#             if city[m][n] == 1:
#                 temp = sys.maxsize
#                 for j in range(M):
#                     temp = min(temp, abs(m - chicken_nCr[i][j][0]) + abs(n - chicken_nCr[i][j][1]))
#                 distance += temp
#     min_distance = min(min_distance, distance)
#
# print(min_distance)
#

from itertools import combinations

## 맵크기(N), 치킨집 최대 선택가능개수(M)
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

## 빈칸(0), 집(1), 치킨집(2)
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

minv = float('inf')
for ch in combinations(chicken, M):
    print(ch)
    sumv = 0
    for home in house:
        sumv += min([abs(home[0] - i[0]) + abs(home[1] - i[1]) for i in ch])
        if minv <= sumv: break
    if sumv < minv: minv = sumv

print(minv)