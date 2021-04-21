import sys

input = sys.stdin.readline
seq_size = int(input())
sequence = list(map(int, input().split()))

dp = [1] * seq_size  # 증가하는 부분 수열 길이
dp2 = [1] * seq_size  # 감소하는 부분 수열 길이

# 증가
for i in range(seq_size):
    for front in range(i):
        if sequence[i] > sequence[front]:
            dp[i] = max(dp[i], dp[front] + 1)

# 감소
for i in range(seq_size - 1, -1, -1):
    for back in range(i + 1, seq_size):
        if sequence[i] > sequence[back]:
            dp2[i] = max(dp2[i], dp2[back] + 1)

# print(dp)
# print(dp2)

ans = []
for a, b in zip(dp, dp2):
    ans.append(a + b)

print(max(ans) - 1)
