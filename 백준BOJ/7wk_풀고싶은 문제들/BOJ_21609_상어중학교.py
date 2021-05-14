import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[False] * N for _ in range(N)]


def find_best_block():
    q = deque([])
    blocks = []
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and board[x][y] > 0:
                visited[x][y] = True
                q.append((x, y))
                least = 1
                block_cnt = 1
                rainbow_cnt = 0
                basisX, basisY = x, y
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx, ny = x + dir[i][0], y + dir[i][1]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            if board[nx][ny] == board[x][y]:
                                block_cnt += 1
                                least += 1
                                q.append((nx, ny))
                                visited[nx][ny] = True
                            elif board[nx][ny] == 0:
                                rainbow_cnt += 1
                                q.append((nx, ny))
                if least >= 2:
                    blocks.append((block_cnt, rainbow_cnt, basisX, basisY))

    return blocks


arr = find_best_block()
for a in arr:
    print(a)
