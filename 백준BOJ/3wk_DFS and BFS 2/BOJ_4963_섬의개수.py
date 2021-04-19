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
            # 지도 안에 있으면서
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):
                # 방문하지 않았고, 땅인 지점만 (--> 섬을 찾기 위한 과정)
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
                # bfs() 1번 수행되면 섹터(섬의 영역 = 이어진 땅들의 모임) 1개가 추가된다.
                sector += 1

    print(sector)
