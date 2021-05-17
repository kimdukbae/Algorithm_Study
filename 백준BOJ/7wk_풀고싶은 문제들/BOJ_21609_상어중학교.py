# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
#
# dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# visited = [[False] * N for _ in range(N)]
#
#
# def find_best_block():
#     q = deque([])
#     blocks = []
#     for x in range(N):
#         for y in range(N):
#             if not visited[x][y] and board[x][y] > 0:
#                 visited[x][y] = True
#                 q.append((x, y))
#                 least = 1
#                 block_cnt = 1
#                 rainbow_cnt = 0
#                 basisX, basisY = x, y
#                 while q:
#                     x, y = q.popleft()
#                     for i in range(4):
#                         nx, ny = x + dir[i][0], y + dir[i][1]
#                         if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#                             if board[nx][ny] == board[x][y]:
#                                 block_cnt += 1
#                                 least += 1
#                                 q.append((nx, ny))
#                                 visited[nx][ny] = True
#                             elif board[nx][ny] == 0:
#                                 rainbow_cnt += 1
#                                 q.append((nx, ny))
#                 if least >= 2:
#                     blocks.append((block_cnt, rainbow_cnt, basisX, basisY))
#
#     return blocks
#
#
# arr = find_best_block()
# for a in arr:
#     print(a)


from collections import deque


def get_group():
    # 현 상태에서 제거할 그룹 선택 > 기준 블록 반환
    chk = [[0 for _ in range(N)] for _ in range(N)]
    chk_num = 0
    group_cnt, group_rainbow_cnt, group_x, group_y = 0, 0, -1, -1  # 그룹 블록 수, 기준블록x, 기준블록y
    for i in range(N):
        for j in range(N):  # 이 순서로 탐색해야 기준 블럭이 생김
            if board[i][j] > 0 and not chk[i][j]:  # 방문하지 않은 일반 블록
                chk_num += 1
                que = deque()
                que.append([i, j])
                chk[i][j] = chk_num
                cnt = 1
                rainbow_cnt = 0
                while que:
                    [x, y] = que.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N and chk[nx][ny] != chk_num:
                            if board[nx][ny] == 0 or board[nx][ny] == board[i][j]:
                                # 무지개 블록 또는 동일 색 일반 블록
                                que.append([nx, ny])
                                chk[nx][ny] = chk_num
                                cnt += 1
                                if board[nx][ny] == 0:
                                    rainbow_cnt += 1
                if cnt > group_cnt:
                    group_cnt, group_rainbow_cnt = cnt, rainbow_cnt
                    group_x, group_y = i, j
                elif cnt == group_cnt:
                    if rainbow_cnt > group_rainbow_cnt:
                        group_cnt, group_rainbow_cnt = cnt, rainbow_cnt
                        group_x, group_y = i, j
                    elif rainbow_cnt == group_rainbow_cnt:
                        if group_x < i or (group_x == i and group_y < j):
                            group_cnt, group_rainbow_cnt = cnt, rainbow_cnt
                            group_x, group_y = i, j

    # print("delete group", (group_x, group_y))

    # 선택한 그룹 제거
    # print()
    # print("DELETING:")
    match = board[group_x][group_y]  # 블록색
    chk = [[False for _ in range(N)] for _ in range(N)]
    que = deque()
    que.append([group_x, group_y])
    board[group_x][group_y] = -2
    chk[group_x][group_y] = True
    while que:
        [x, y] = que.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not chk[nx][ny] and (board[nx][ny] == match or board[nx][ny] == 0):
                que.append([nx, ny])
                board[nx][ny] = -2
                chk[nx][ny] = True
    # for b in board:
    #     print(*b)
    # print()

    return group_cnt


def set_gravity():
    # 중력 적용
    # print()
    # print("DROPPING:", direction)
    for j in range(N):  # 모든 열에 대해서
        tmp = [-2 for _ in range(N)]
        collapse, cur = 0, 0
        for i in range(N - 1, -1, -1):
            if board[i][j] >= 0:
                tmp[collapse] = board[i][j]
                collapse += 1
                cur += 1
            elif board[i][j] == -1:
                tmp[cur] = -1
                cur += 1
                collapse = cur
            elif board[i][j] == -2:
                cur += 1
        # print(j, "열", tmp)
        for i in range(N):
            board[i][j] = tmp[N - 1 - i]

    # for b in board:
    #     print(*b)
    return


def turn():
    # print("\nTURNING")
    global board, N
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res[N - j - 1][i] = board[i][j]
    board = res

    # for b in board:
    #     print(*b)


N, M = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))  # -2: 빈칸, -1: 검은색, 0: 무지개색, 1~: 일반
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]  # v > ^ <
score = 0

while True:
    add = get_group()
    # print(">>>>>>>>>>>>>>>>> add", add**2)
    if add <= 1:
        break
    score += pow(add, 2)
    set_gravity()
    turn()
    set_gravity()

print(score)
