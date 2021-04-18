# Python3 / PyPy3 모두 시간 초과
# 1. 보석(무게, 가격)은 가격 기준 내림차순으로 정렬
# 2. 가방은 담을 수 있는 최대 무게를 오름차순으로 정렬
# 3. 보석의 무게 <= 가방의 무게이면 가방에 담아서 훔치는 걸로 처리
# 4. 3번 과정 반복
# import sys
#
# input = sys.stdin.readline
# N, K = map(int, input().split())
# jewels = []
# for _ in range(N):
#     x, y = map(int, input().split())
#     jewels.append((x, y))
# jewels = sorted(jewels, key=lambda x: -x[1])
# visited_jewels = [False] * N
#
# backpacks = []
# for _ in range(K):
#     backpacks.append(int(input()))
# backpacks = sorted(backpacks)
# visited_backpacks = [False] * K
#
# ans = 0
# for i in range(len(backpacks)):
#     for k in range(len(jewels)):
#         if jewels[k][0] <= backpacks[i] and not visited_backpacks[i] and not visited_jewels[k]:
#             ans += jewels[k][1]
#             visited_jewels[k] = True
#             visited_backpacks[i] = True
#
# print(ans)


# --------------------------------------------------------------------------------------------------
# 다른 풀이가 필요 --> 우선순위 큐를 써야함 --> 왜 우선순위 큐를 써야하지? --> 시간복잡도 낮추려고!
import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())
jewels = []
for _ in range(N):
    heapq.heappush(jewels, list(map(int, input().split())))

backpacks = []
for _ in range(K):
    backpacks.append(int(input()))
backpacks = sorted(backpacks)

ans = 0
possible = []
for backpack in backpacks:
    while jewels and backpack >= jewels[0][0]:
        heapq.heappush(possible, -heapq.heappop(jewels)[1])
    if possible:
        ans -= heapq.heappop(possible)

print(ans)
