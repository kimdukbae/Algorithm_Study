import sys

input = sys.stdin.readline

n, x, y = map(int, input().split())

seq = [0] * (2 * n + 1)
seq[x] = seq[y] = y - x - 1
answer = 0


def dfs(depth):
    global answer

    if depth == (y - x - 1):
        dfs(depth + 1)

    if depth == n + 1:
        answer += 1
        return

    for i in range(1, len(seq) - depth - 1):
        if seq[i] == 0 and seq[i + depth + 1] == 0:
            seq[i] = seq[i + depth + 1] = depth
            dfs(depth + 1)
            seq[i] = seq[i + depth + 1] = 0


dfs(1)
print(answer)
