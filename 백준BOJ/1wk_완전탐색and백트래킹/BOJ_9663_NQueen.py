import sys

input = sys.stdin.readline
N = int(input())
a, b, c = [0] * N, [0] * (2 * N - 1), [0] * (2 * N - 1)
result = 0


# depth는 행
def dfs(depth):
    global result
    if depth == N:
        result += 1
        return
    # col는 열
    for col in range(N):
        # a,b,c 배열을 이용해 서로의 퀸이 공격할 수 없는 위치를 정한다.
        if not a[col] and not b[depth + col] and not c[depth - col + N - 1]:
            a[col] = b[depth + col] = c[depth - col + N - 1] = 1
            dfs(depth + 1)  # 다음 행으로 탐색 진행
            a[col] = b[depth + col] = c[depth - col + N - 1] = 0


dfs(0)
print(result)
