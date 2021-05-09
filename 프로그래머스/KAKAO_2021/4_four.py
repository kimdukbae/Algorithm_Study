import heapq


# 방의 개수 n / 출발 start / 도착 end / 통로와 이동시간 정보 / 함정 traps
def solution(n, start, end, roads, traps):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    cost = [1e9] * (n + 1)
    for i in range(len(roads)):
        first, second, time = roads[i]
        graph[first].append((second, time))  # (시간, f -> s으로 가는 경로)

    search(start, graph, cost, traps, n)

    answer = cost[end]
    return answer


def search(start, graph, cost, traps, n):
    q = []
    heapq.heappush(q, (0, start))
    cost[start] = 0
    basis = graph

    while q:
        reverse_graph = [[] for _ in range(n + 1)]
        dist, now = heapq.heappop(q)
        if now in traps:
            for x in range(1, n + 1):
                if x == i[0]:
                    for j in range(len(basis[x])):
                        reverse_graph[basis[x][j][0]].append((x, basis[x][j][1]))
                else:
                    for j in range(len(basis[x])):
                        reverse_graph[i[0]].append((x, basis[x][j][1]))

            basis = reverse_graph

        if cost[now] < dist:
            continue
        for i in basis[now]:
            temp = dist + i[1]
            if i[0] in traps:
                for x in range(1, n + 1):
                    if x == i[0]:
                        for j in range(len(basis[x])):
                            reverse_graph[basis[x][j][0]].append((x, basis[x][j][1]))
                    else:
                        for j in range(len(basis[x])):
                            reverse_graph[i[0]].append((x, basis[x][j][1]))

            if temp < cost[i[0]]:
                cost[i[0]] = temp
                heapq.heappush(q, (temp, i[0]))
        basis = reverse_graph


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
