import sys

input = sys.stdin.readline
L, K, C = map(int, input().split())
cut = list(map(int, input().split()))
log = [0] * L

for c in cut:
    log[c - 1] = 1




