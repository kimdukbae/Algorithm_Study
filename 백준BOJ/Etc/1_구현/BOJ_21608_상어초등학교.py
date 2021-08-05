import sys

input = sys.stdin.readline
N = int(input())
board = [[-1] * N for _ in range(N)]

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

student = {}
for _ in range(N * N):
    like_list = list(map(int, input().split()))
    student[like_list[0]] = like_list[1:]

    seatX, seatY = 0, 0
    maximum_like, maximum_empty = -1, -1

    # 자리 정하기
    for x in range(N):
        for y in range(N):
            if board[x][y] == -1:
                like = 0
                empty = 0
                for i in range(4):
                    nx, ny = x + dir[i][0], y + dir[i][1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] in like_list[1:]:
                            like += 1
                        elif board[nx][ny] == -1:
                            empty += 1
                if maximum_like < like or (maximum_like == like and maximum_empty < empty):
                    seatX, seatY = x, y
                    maximum_like, maximum_empty = like, empty

    board[seatX][seatY] = like_list[0]

# for b in board:
#     print(b)
# print(student)

# 만족도 총합
answer = 0
for x in range(N):
    for y in range(N):
        cnt = 0
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] in student[board[x][y]]:
                cnt += 1
        if cnt != 0:
            answer += 10 ** (cnt - 1)

print(answer)
