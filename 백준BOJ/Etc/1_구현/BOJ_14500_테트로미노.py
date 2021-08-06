import sys

input = sys.stdin.readline
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# for b in board:
#     print(b)

tetrominos = [
    # 1자
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],

    # ㅁ자
    [(0, 0), (0, 1), (1, 0), (1, 1)],

    # ㄴ자
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (-1, 1), (-2, 1)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],

    # ㄹ자
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    [(0, 0), (1, 0), (1, -1), (2, -1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],

    # ㅗ자
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, -1)]
]

answer = 0
for x in range(N):
    for y in range(M):
        for tetromino in tetrominos:
            mid_sum = 0
            for i in range(len(tetromino)):
                nx, ny = x + tetromino[i][0], y + tetromino[i][1]
                if 0 <= nx < N and 0 <= ny < M:
                    mid_sum += board[nx][ny]

            answer = max(answer, mid_sum)

print(answer)
