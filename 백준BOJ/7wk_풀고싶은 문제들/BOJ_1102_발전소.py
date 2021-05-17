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


# 민서님
def get(cur):
    # cur 상태에서 발전기를 다(P개) 키려면 필요한 최소 비용 반환
    global cnt
    if cnt >= P:  # 필요한 발전기를 다 켰다면
        return 0
    if mem[cur] != -1:  # 이미 계산되어 있다면
        return mem[cur]
    ret = float('inf')
    cnt += 1
    for i in range(N):
        if cur & (1 << i):  # i가 켜진 상태라면 i로 킬 수 있는 발전기 키기
            for j in range(N):
                if not (cur & (1 << j)):  # j는 안켜진 발전기
                    ret = min(ret, get(cur | (1 << j)) + cost[i][j])  # j를 안키는 것 vs. j를 키고 이 상태에서 다 키는 것
    cnt -= 1
    mem[cur] = ret
    return mem[cur]


N = int(input())
cost = list(list(map(int, input().split())) for  in range(N))
cnt, state = 0, 0
mem = [-1 for  in range(1 << (N + 1) - 1)]  # mem[i]: i 상태가 되기 위해 필요한 최소 비용
for i, n in enumerate(list(map(str, input()))):
    if n == "Y":
        cnt += 1
        state |= 1 << i
P = int(input())
ans = get(state)
print(ans if ans != float('inf') else -1)

