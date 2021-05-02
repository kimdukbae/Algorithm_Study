import sys

input = sys.stdin.readline
N = int(input())
elevator = [list(input().rstrip()) for _ in range(5)]

for e in elevator:
    print(*e)