def solution(n, computers):
    graph = [[] for _ in range(n)]
    visited = [0] * n

    # 딕셔너리로도 인접 리스트 구현 가능
    # graph = {i : [] for i in range(n)} --> 노드번호가 1번으로 시작할 때
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif computers[i][j] == 1:
                graph[i].append(j)

    group = 1
    for i in range(n):
        dfs(graph, visited, i, group)
        group += 1

    return len(set(visited))


def dfs(graph, visited, start, group):
    if not visited[start]:
        visited[start] = group

    for g in graph[start]:
        if not visited[g]:
            dfs(graph, visited, g, group)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
