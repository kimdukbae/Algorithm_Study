import sys
from collections import deque

input = sys.stdin.readline
V, E, start = map(int, input().split())
connection = [list(map(int, input().split())) for _ in range(E)]
visited = [False] * (V + 1)

graphs = [[] for _ in range(V + 1)]
for connect in connection:
    graphs[connect[0]].append(connect[1])
    graphs[connect[1]].append(connect[0])

# 정점이 여러 개인 경우에는 정점 번호가 작은 것부터 방문하기 위한 정렬
# 인접 행렬로 구현하면 순차적으로 탐색하여 정렬해줄 필요가 없음.
# 하지만 인접 리스트로 구현하면 아래와 같이 정렬해줘야함.
for i in range(len(graphs)):
    graphs[i].sort()


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    for g in graph[start]:
        if not visited[g]:
            dfs(graph, g, visited)


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for g in graph[cur]:
            if not visited[g]:
                visited[g] = True
                q.append(g)


dfs(graphs, start, visited)
print()
visited = [False] * (V + 1)     # DFS 때 사용했던 방문 리스트 초기화 (BFS 탐색에 필요하기 때문에 초기화)
bfs(graphs, start, visited)
