import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
aqua = [list(map(int, input().split())) for _ in range(N)]

size = 2
sx, sy = 0, 0
# 아기상어 출발 시작점 찾기 (1번만 수행)
for r in range(N):
    for c in range(N):
        if aqua[r][c] == 9:
            sx, sy = r, c
            aqua[r][c] = 0

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# 현재 아기상어 위치에서 최단거리 테이블을 계산하는 함수
def bfs():
    distance = [[-1] * N for _ in range(N)]
    q = deque([(sx, sy)])
    distance[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < N and 0 <= ny < N:
                if distance[nx][ny] == -1 and aqua[nx][ny] <= size:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

    return distance

# 계산된 거리테이블과 크기테이블을 통해 먹을 물고기 탐색 (공간안에 있고 아기상어 크기보다 작은 물고기만 먹게)
def hunt(distance):
    minimum = 1e9
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if distance[i][j] != -1 and 1 <= aqua[i][j] < size:
                if distance[i][j] < minimum:
                    x, y = i, j
                    minimum = distance[i][j]

    if minimum == 1e9:
        return 0
    else:
        return x, y, minimum


answer = 0
count = 0
while True:
    fish = hunt(bfs())
    if fish == 0:
        print(answer)
        break
    else:
        sx, sy = fish[0], fish[1]
        answer += fish[2]
        aqua[sx][sy] = 0
        count += 1
        if count == size:
            size += 1
            count = 0
