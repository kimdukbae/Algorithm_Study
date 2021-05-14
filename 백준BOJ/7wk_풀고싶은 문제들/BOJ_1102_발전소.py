# 너무 어렵다...
import sys

input = sys.stdin.readline
N = int(input())
costs = []
for _ in range(N):
    i, j, cost = map(int, input().split())
    costs.append([i, j, cost])

string = input().rstrip()
P = int(input())

time = on_off = 0
for i in range(len(string)):
    if string[-i - 1] == "Y":
        on_off += 2 ** i
        time += 1

