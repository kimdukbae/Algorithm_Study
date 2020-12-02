N, M = map(int, input().split())
r, c, direction = map(int, input().split())
visited = [[0] * M for _ in range(N)]
board = [[0] * M for _ in range(N)]

for i in range(N):
    board[i] = list(map(int, input().split()))

def turn_left():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3

# 북, 동, 남, 서
dir = [[-1, 0], [0, 1], [1, 0] ,[0, -1]]
ans = 0
turn_time = 0

while True:
    turn_left()
    nr = r + dir[direction][0]
    nc = c + dir[direction][1]

    if visited[nr][nc] == 0 and board[nr][nc] == 0:
        visited[nr][nc] = 1
        r = nr
        c = nc
        ans += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    if turn_time == 4:
        nr = r - dir[direction][0]
        nc = c - dir[direction][1]

        if board[nr][nc] == 0:
            r = nr
            c = nc

        else:
            break

        turn_time = 0

print(ans)