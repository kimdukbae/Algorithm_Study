# 내 풀이
N, M = map(int, input().split())
x, y, direction = map(int, input().split())
dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
board = [0 for i in range(N)]

for i in range(N):
    board[i] = list(map(int, input().split()))

while True:


