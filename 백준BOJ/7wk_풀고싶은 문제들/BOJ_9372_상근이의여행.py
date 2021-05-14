import sys

input = sys.stdin.readline


def dfs(start):
    global answer
    for g in graph[start]:
        if not visited[g]:
            visited[g] = True
            answer += 1
            dfs(g)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N + 1)
    answer = 0
    visited[1] = True
    dfs(1)

    print(answer)
