# 답을 참고하면서 구현했는데 왜 틀린지를 모르겠다...
# import sys
#
# N = int(sys.stdin.readline())
# K = int(sys.stdin.readline())
#
# board = [[0] * (N + 1) for _ in range(N + 1)]
# for i in range(K):
#     a, b = map(int, sys.stdin.readline().split())
#     board[a][b] = 1
#
# route = []
# L = int(sys.stdin.readline())
# for i in range(L):
#     x, c = sys.stdin.readline().split()
#     route.append((int(x), c))
#
# # 동남서북 (처음에 오른쪽 보고 있어서 그렇다고함)
# dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#
#
# def turn(direction, ch):
#     if ch == 'L':
#         direction = (direction - 1) % 4
#     else:
#         direction = (direction + 1) % 4
#     return direction
#
#
# def simulation():
#     x, y = 1, 1
#     board[x][y] = 2
#     direction = 0
#     time = 0
#     idx = 0
#     snake = [(x, y)]
#
#     while True:
#         nx = x + dir[direction][0]
#         ny = y + dir[direction][1]
#
#         # 맵의 범위 안에 있으면서 뱀의 몸통과 안 부딫히면
#         if 1 <= nx <= N and 1 <= ny <= N and board[nx][ny] != 2:
#             # 사과가 없다면 이동 후 꼬리 제거
#             if board[nx][ny] == 0:
#                 board[nx][ny] = 2
#                 snake.append((nx, ny))
#                 px, py = snake.pop(0)
#                 board[px][py] = 0
#
#             # 사과가 있다면 이동 후 꼬리 그대로
#             if board[nx][ny] == 1:
#                 board[nx][ny] = 2
#                 snake.append((nx, ny))
#
#         # 벽 혹은 뱀의 몸통과 부딫혔다면
#         else:
#             time += 1
#             break
#
#         x, y = nx, ny
#         time += 1
#         if idx < K and time == route[idx][0]:
#             direction = turn(direction, route[idx][1])
#             idx += 1
#
#     return time
#
#
# print(simulation())

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())