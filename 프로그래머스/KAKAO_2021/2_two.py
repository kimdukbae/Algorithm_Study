from collections import deque


def find_target(arr):
    target = []

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'P':
                target.append((i, j))

    return target


def solution(places):
    answer = []
    board = [[['0'] * 5 for _ in range(5)] for _ in range(len(places))]

    for i in range(len(places)):
        for r in range(len(places[i])):
            for c in range(len(places[i][0])):
                board[i][r][c] = places[i][r][c]

    # 출력
    # for b in board:
    #     for x in b:
    #         print(x)
    #     print()

    dir1 = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dir2 = [[-1, -1], [1, -1], [-1, 1], [1, 1]]

    for i in range(len(board)):
        XY, q = [], deque()
        XY = find_target(board[i])
        for xy in XY:
            q.append(xy)
        flag = True

        while q:
            x, y = q.popleft()
            for d in range(4):
                nx, ny = x + dir1[d][0], y + dir1[d][1]
                nnx, nny = x + dir1[d][0] * 2, y + dir1[d][1] * 2
                # 1
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if board[i][nx][ny] == 'P':
                        flag = False
                    if 0 <= nnx < 5 and 0 <= nny < 5 and board[i][nnx][nny] == 'P' and board[i][nx][ny] != 'X':
                        flag = False

            for d in range(4):
                nx, ny = x + dir2[d][0], y + dir2[d][1]
                if 0 <= nx < 5 and 0 <= ny < 5 and board[i][nx][ny] == 'P':
                    if board[i][x + dir2[d][0]][y] != 'X' or board[i][x][y + dir2[d][1]] != 'X':
                        flag = False

        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
