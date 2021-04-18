# PyPy3만 통과 / Python3 시간초과
import sys

input = sys.stdin.readline
n, x, y = map(int, input().split())
ans = 0
explore = [0] * (2 * n + 1)
explore[x] = explore[y] = y - x - 1


def dfs(depth):
    global ans
    if depth == (y - x - 1):
        dfs(depth + 1)

    if depth == n + 1:
        ans += 1
        # print(explore)
        return

    for i in range(1, len(explore) - depth - 1):
        if explore[i] == 0 and explore[i + depth + 1] == 0:
            explore[i] = explore[i + depth + 1] = depth
            dfs(depth + 1)
            explore[i] = explore[i + depth + 1] = 0


dfs(1)
print(ans)
