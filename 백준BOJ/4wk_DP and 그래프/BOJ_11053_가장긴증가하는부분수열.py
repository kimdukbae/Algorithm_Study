import sys

# 분할 정복 (이진 탐색) 으로 풀 수 있음
input = sys.stdin.readline
seq_size = int(input())
sequence = list(map(int, input().split()))

# 현재 자신을 포함하여 만들 수 있는 LIS 길이 저장
# (자기 자신을 포함하므로 dp 리스트 1로 초기화)
dp = [1] * seq_size

# i를 기준으로
for i in range(seq_size):
    # i보다 인덱스가 작은 모든 원소들 전부 탐색
    for j in range(i):
        # LIS 만들기
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 잘못된 방법
# cur = sequence[0]
# ans = [sequence[0]]
# 반례 --> 10 21 1 10 20 30 40 50 60
# 답 7인데 6이 나와버림
# for i in range(1, len(sequence)):
#     if cur < sequence[i]:
#         cur = sequence[i]
#         ans.append(sequence[i])
#
# print(len(ans))
