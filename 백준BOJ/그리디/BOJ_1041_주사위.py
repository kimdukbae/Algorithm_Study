import sys

input = sys.stdin.readline
N = int(input())
dice = list(map(int, input().split()))
ans = 0

# if N == 1:
#     ans = dice[0] + dice[1] + dice[2] + dice[3] + dice[4] + dice[5]
# elif N == 2:
#     ans = ((dice[0] * N * N) + (dice[1] * N * 2) + (dice[2] * N)) * N
# else:
#     ans = ((dice[0] * N * N) + (dice[1] * N * 2) + (dice[2] * N)) * (N - 1) + (dice[0] * N * 3 * (N - 2))
#
# print(ans)


if N == 1:
    for i in range(len(dice) - 1):
        ans += dice[i]

else:
