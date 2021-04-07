# https://rebas.kr/790
import sys

input = sys.stdin.readline
N, M, H = map(int, input().split())
ladder = [[0] * N for _ in range(H)]
ans = 4

for i in range(M):
    r, c = map(int, input().split())
    ladder[r - 1][c - 1] = 1


def move():
    for n in range(N):
        start = n
        for h in range(H):
            if ladder[h][start]:  # 우측이동
                start += 1
            elif start > 0 and ladder[h][start - 1]:  # 좌측이동
                start -= 1
        if start != n:
            return False
    return True


def dfs(cnt, x, y):
    global ans
    if ans <= cnt:
        return
    if move():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    for i in range(x, H):
        k = y if i == x else 0
        for j in range(k, N - 1):
            if ladder[i][j]:
                j += 1
            else:
                ladder[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                ladder[i][j] = 0


dfs(0, 0, 0)
print(ans if ans < 4 else -1)



# 사다리 인덱스 바꿔서 맨 마지막 행 배열 시작점=도착점 같은지 보는걸로

