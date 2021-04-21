import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]
ans = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    v1, v2, route = map(int, input().split())
    graph[v1][v2] = route
    graph[v2][v1] = route
    ans[v1][v2] = v2
    ans[v2][v1] = v1

for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            print('-', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

for c in ans:
    print(c)