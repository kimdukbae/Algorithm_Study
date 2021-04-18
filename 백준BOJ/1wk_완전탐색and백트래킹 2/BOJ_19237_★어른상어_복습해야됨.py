import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
shark_dir = list(map(int, input().split()))  # 4 4 3 1

smell = [[[0, 0]] * N for _ in range(N)]  # 상황판

priority = [[] for _ in range(M)]
for i in range(M):
    for j in range(4):
        priority[i].append(list(map(int, input().split())))

# print(priority)

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상 하 좌 우


def update_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if sea[i][j] != 0:
                smell[i][j] = [sea[i][j], K]


def move():
    new_sea = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if sea[r][c] != 0:
                direction = shark_dir[sea[r][c] - 1]
                flag = False
                for i in range(4):
                    nr = r + dir[priority[sea[r][c] - 1][direction - 1][i] - 1][0]
                    nc = c + dir[priority[sea[r][c] - 1][direction - 1][i] - 1][1]
                    if 0 <= nr < N and 0 <= nc < N:
                        if smell[nr][nc][1] == 0:
                            shark_dir[sea[r][c] - 1] = priority[sea[r][c] - 1][direction - 1][i]
                        if new_sea[nr][nc] == 0:
                            new_sea[nr][nc] = sea[r][c]
                        else:
                            new_sea[nr][nc] = min(new_sea[nr][nc], sea[r][c])  # 번호가 낮은 상어가 들어가도록
                        flag = True
                        break

                if flag:
                    continue

                for i in range(4):
                    nr = r + dir[priority[sea[r][c] - 1][direction - 1][i] - 1][0]
                    nc = c + dir[priority[sea[r][c] - 1][direction - 1][i] - 1][1]
                    if 0 <= nr < N and 0 <= nc < N:
                        if smell[nr][nc][0] == sea[r][c]:
                            shark_dir[sea[r][c] - 1] = priority[sea[r][c] - 1][direction - 1][i]
                            new_sea[nr][nc] = sea[r][c]
                            break

    return new_sea


time = 0
while True:
    update_smell()
    new_sea = move()
    sea = new_sea
    time += 1

    check = True
    for i in range(N):
        for j in range(N):
            if sea[i][j] > 1:
                check = False

    if check:
        print(time)

    if time >= 1000:
        print(-1)
        break
