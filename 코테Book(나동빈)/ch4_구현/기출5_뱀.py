import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

board = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x][y] = 1

route = []
L = int(sys.stdin.readline())
for i in range(L):
    x, c = sys.stdin.readline().split()
    route.append((int(x), c))

# 동남서북 (처음에 오른쪽 보고 있어서 그렇다고함)
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulation():
    sx, sy = 1, 1
    board[sx][sy] = 2
    direction = 0  # 동쪽
    time = 0
    idx = 0
    snake = [(sx, sy)]

    while True:
        nx, ny = sx + dir[direction][0], sy + dir[direction][1]

        # 맴 범위안에 있고, 자기자신과 안 부딫힌다면
        if 1 <= nx <= N and 1 <= ny <= N and board[nx][ny] != 2:
            # 사과가 없다면 이동 후 꼬리 제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                snake.append((nx, ny))
                px, py = snake.pop(0)
                board[px][py] = 0

            # 사과가 있다면 이동 후 꼬리 남겨둠
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                snake.append((nx, ny))

        # 벽 or 자기자신과 부딫혔다면
        

