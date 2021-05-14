# 너무 어렵다... --> DP + 비트마스킹
import sys

input = sys.stdin.readline
N = int(input())
costs = []
for _ in range(N):
    i, j, cost = map(int, input().split())
    costs.append([i, j, cost])

string = input().rstrip()
P = int(input())

# https://velog.io/@qweadzs/BOJ-1102-%EB%B0%9C%EC%A0%84%EC%86%8CPython
time = on_off = 0
for i in range(len(string)):
    if string[-i - 1] == "Y":
        on_off += 2 ** i
        time += 1


