import sys

input = sys.stdin.readline
N, K = map(int, input().split())
coin = []
ans = 0

for i in range(N):
    coin.append(int(input().rstrip()))

for i in range(N - 1, -1, -1):
    if coin[i] > K:
        continue
    ans += K // coin[i]
    K %= coin[i]

print(ans)
