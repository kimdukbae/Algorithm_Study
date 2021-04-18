import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
dir = [[-2, -1], [-1, -2], [2, -1], [1, -2], [2, 1], [1, 2], [-2, 1], [-1, 2]]


def bfs(arr, sx, sy, ex, ey):
    if sx == ex and sy == ey:
        return 0

    q = deque([(sx, sy)])
    arr[sx][sy] = 1
    ans = 1

    while q:
        size = len(q)
        # 나이트가 최소 몇 번 움직이는지 구해주기 위한 for 문
        for s in range(size):
            x, y = q.popleft()
            for i in range(8):
                nx, ny = x + dir[i][0], y + dir[i][1]
                if nx == ex and ny == ey:
                    return ans

                elif 0 <= nx < len(arr) and 0 <= ny < len(arr) and not arr[nx][ny]:
                    arr[nx][ny] = 1
                    q.append((nx, ny))

        ans += 1

    return ans


for _ in range(T):
    I = int(input())

    chess = [[0] * I for _ in range(I)]
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())

    print(bfs(chess, startX, startY, endX, endY))
