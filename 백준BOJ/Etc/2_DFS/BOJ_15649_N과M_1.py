import sys

input = sys.stdin.readline
N, M = map(int, input().split())
visited = [False] * (N + 1)
result = []


def N_M(depth, N, M):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N + 1):
        if visited[i]:
            continue
        visited[i] = True
        result.append(i)
        N_M(depth + 1, N, M)
        visited[i] = False;
        result.pop()


N_M(0, N, M)
