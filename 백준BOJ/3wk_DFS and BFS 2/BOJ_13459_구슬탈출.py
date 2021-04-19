import sys
from collections import deque

input = sys.stdin.readline
row, col = map(int, input().split())
board = [list(input().rstrip()) for _ in range(row)]

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
redX, redY, blueX, blueY = 0, 0, 0, 0

for r in range(row):
    for c in range(col):
        if board[r][c] == 'R':
            redX, redY = r, c
        elif board[r][c] == 'B':
            blueX, blueY = r, c


def bfs():
    q_red = deque([])
    q_blue = deque([])
