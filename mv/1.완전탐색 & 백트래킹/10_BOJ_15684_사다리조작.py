import sys

input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[0] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a - 1][b - 1] = 1  # 사다리의 좌측좌표만 표시

answer = 4


def move():
    for c in range(N):
        start = c
        for r in range(H):
            # 우측 이동
            if ladder[r][start]:
                start += 1
            # 좌측 이동
            elif start > 0 and ladder[r][start - 1]:
                start -= 1

        if start != c:
            return False

    return True


def dfs(cnt, x, y):
    global answer

    if answer <= cnt:
        return
    if move():
        answer = min(answer, cnt)
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


# for l in ladder:
#     print(l)
dfs(0, 0, 0)
print(answer if answer < 4 else -1)
