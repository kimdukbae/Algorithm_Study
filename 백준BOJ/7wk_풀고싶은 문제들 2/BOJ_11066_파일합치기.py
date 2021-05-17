# 민서님 코드
def dp(s, e):
    if s == e:
        return 0
    if mem[s][e] != 1e9:
        return mem[s][e]
    ans = 1e9
    for m in range(s, e):
        ans = min(ans, dp(s, m) + dp(m + 1, e) + cum_sum[e + 1] - cum_sum[s])
    mem[s][e] = ans
    return mem[s][e]


for _ in range(int(input())):
    K = int(input())
    size = list(map(int, input().split()))
    cum_sum = [0]
    for s in size:
        cum_sum.append(cum_sum[-1] + s)
    mem = list(list(1e9 for _ in range(K)) for _ in range(K))  # mem[a][b]: a에서 b까지 파일을 합치는 최소 비용
    print(dp(0, K - 1))
