import sys
from collections import deque

input = sys.stdin.readline
N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs():
    count = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dir[d][0]
            nc = c + dir[d][1]
            if 0 <= nr < 2 ** N and 0 <= nc < 2 ** N and not visited[nr][nc] and A[nr][nc] != 0:
                count += 1
                q.append((nr, nc))
                visited[nr][nc] = True

    return count


for i in range(Q):
    gap = 2 ** L[i]
    for x in range(0, N, gap):
        for y in range(0, N, gap):
            rotate = [A[i][y:y + gap] for i in range(x, x + gap)]
            for r in range(gap):
                for c in range(gap):
                    # print((r, c), '-->', (x + c, y + gap - 1 - r))
                    A[x + c][y + gap - 1 - r] = rotate[r][c]

    for x in range(2 ** N):
        for y in range(2 ** N):
            cnt = 0
            for d in range(4):
                nx = x + dir[d][0]
                ny = y + dir[d][1]
                if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N and A[nx][ny] != 0:
                    cnt += 1
            if cnt < 3 and A[x][y] > 0:
                A[x][y] -= 1

q = deque()
visited = [[False] * (2 ** N) for _ in range(2 ** N)]
answer = 0
for x in range(2 ** N):
    for y in range(2 ** N):
        if not visited[x][y] and A[x][y] != 0:
            visited[x][y] = True
            q.append((x, y))
            answer = max(answer, bfs())

for a in A:
    print(a)
print(sum(sum(a) for a in A))
print(answer)
