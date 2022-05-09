import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewelries = []
for _ in range(N):
    heapq.heappush(jewelries, list(map(int, input().split())))

backpacks = []
for _ in range(K):
    heapq.heappush(backpacks, int(input()))
backpacks = sorted(backpacks)

answer = 0
possible = []
for backpack in backpacks:
    while jewelries and backpack >= jewelries[0][0]:
        heapq.heappush(possible, -heapq.heappop(jewelries)[1])
    if possible:
        answer -= heapq.heappop(possible)

print(answer)
