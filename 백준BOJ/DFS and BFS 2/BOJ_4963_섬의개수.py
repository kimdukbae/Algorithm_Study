import sys
from collections import deque

input = sys.stdin.readline
dir = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]


def bfs(arr, r, c, visited):
    q = deque([(r, c)])
    visited[r][c] = True

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dir[i][0], y + dir[i][1]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))


while True:
    col, row = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(row)]
    visited = [[False] * col for _ in range(row)]
    sector = 0

    if col == 0 and row == 0:
        break

    for r in range(row):
        for c in range(col):
            if board[r][c] == 1 and not visited[r][c]:
                bfs(board, r, c, visited)
                sector += 1

    print(sector)
