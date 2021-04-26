import sys
from collections import deque

input = sys.stdin.readline
row, col = map(int, input().split())
board = [list(input().rstrip()) for _ in range(row)]

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
