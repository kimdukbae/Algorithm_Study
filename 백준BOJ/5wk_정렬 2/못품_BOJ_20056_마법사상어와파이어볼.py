from collections import deque

new_dir = [[1, 3, 5, 7], [0, 2, 4, 6]]
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]  # 이동방향
sharks = deque()
# Initialize
N, M, K = map(int, input().split())
board = list(list(deque() for _ in range(N)) for _ in range(N))
for i in range(1, M + 1):
    r, c, m, s, d = map(int, input().split())
    board[r - 1][c - 1].append((m, s, d))
    sharks.append([r - 1, c - 1])

# Start
for _ in range(K):
    # print("\nRIGHT BEFORE MOVING")
    # for b in board:
    #     print(*b)
    cnt = len(sharks)
    for _ in range(cnt):
        r, c = sharks.popleft()
        if not board[r][c]:
            continue
        m, s, d = board[r][c].popleft()
        nr, nc = (r + dx[d] * s) % N, (c + dy[d] * s) % N
        sharks.append([nr, nc])
        board[nr][nc].append((m, s, d))
    # print("\nRIGHT AFTER MOVING:")
    # for b in board:
    #     print(b)
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 1:
                num = len(board[i][j])
                new_mass = 0
                new_speed = 0
                directions = []
                while board[i][j]:
                    m, s, d = board[i][j].pop()
                    new_mass += m
                    new_speed += s
                    directions.append(d)
                new_mass //= 5
                new_speed //= num
                new_direction = all(list(map(lambda x: x % 2 == 0, directions))) | all(list(map(lambda x: x % 2 == 1, directions)))
                if new_mass != 0:
                    for idx in range(4):
                        board[i][j].append((new_mass, new_speed, new_dir[new_direction][idx]))
                        sharks.append([i, j])
    # print("\nAFTER COMBINATION")
    # for b in board:
    #     print(b)

ans = 0
for i in range(N):
    for j in range(N):
        while board[i][j]:
            m, s, d = board[i][j].pop()
            ans += m
print(ans)
