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

#  "i ≥ 2인 경우에 Ai는 Ai-1의 배수" --> 이 조건때문에 K가 무조건 나눠떨어지게 된다.
