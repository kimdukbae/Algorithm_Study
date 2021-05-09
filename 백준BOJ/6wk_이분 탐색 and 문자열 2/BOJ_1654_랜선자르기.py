import sys

input = sys.stdin.readline
K, N = map(int, input().split())
lines = list(int(input()) for _ in range(K))

start, end = 1, max(lines)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for line in lines:
        total += line // mid
    if total >= N:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
