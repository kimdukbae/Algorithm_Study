import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 시작점을 찾아야함
size = 2
sx, sy = 0, 0
for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            sx, sy = r, c
            board[sx][sy] = 0

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]


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
                if distance[nx][ny] == -1 and board[nx][ny] <= size:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

    return distance


# dist = bfs()
# for d in dist:
#     print(d)

def find(distance):
    x, y = 0, 0
    minimum = 1e9
    for i in range(N):
        for j in range(N):
            if 1 <= board[i][j] < size and distance[i][j] != -1:
                if distance[i][j] < minimum:
                    x, y = i, j
                    minimum = distance[i][j]

    if minimum == 1e9:
        return 0
    else:
        return x, y, minimum


ans, count = 0, 0
while True:
    value = find(bfs())
    if value == 0:
        print(ans)
        break
    else:
        ans += value[2]
        sx, sy = value[0], value[1]
        board[sx][sy] = 0
        count += 1
        if count == size:
            size += 1
            count = 0
