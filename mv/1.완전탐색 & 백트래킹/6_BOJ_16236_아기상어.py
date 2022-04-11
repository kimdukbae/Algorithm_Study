import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = 0
size = 2
startX, startY = 0, 0

for r in range(N):
    for c in range(N):
        if sea[r][c] == 9:
            startX, startY = r, c
            sea[startX][startY] = 0


def calculateDistance():
    distance = [[-1] * N for _ in range(N)]
    q = deque([(startX, startY)])
    distance[startX][startY] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dir[k][0]
            ny = y + dir[k][1]
            if 0 <= nx < N and 0 <= ny < N:
                if sea[nx][ny] <= size and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

    return distance


def hunt(distance):
    minimum = 1e9
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if 0 < sea[i][j] < size and minimum > distance[i][j] and distance[i][j] != -1:
                x, y = i, j
                minimum = distance[i][j]

    if minimum == 1e9:
        return 0

    return x, y, minimum


count = 0
while True:
    fish = hunt(calculateDistance())
    if fish == 0:
        print(answer)
        break
    startX, startY = fish[0], fish[1]
    answer += fish[2]
    sea[startX][startY] = 0
    count += 1
    if count == size:
        count = 0
        size += 1
