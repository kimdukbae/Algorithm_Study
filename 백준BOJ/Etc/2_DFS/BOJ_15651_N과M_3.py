import sys

input = sys.stdin.readline
N, M = map(int, input().split())
result = []


# nCr
def N_M(depth, n, r):
    if depth == r:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n + 1):
        result.append(i)
        N_M(depth + 1, n, r)
        result.pop()


N_M(0, N, M)
