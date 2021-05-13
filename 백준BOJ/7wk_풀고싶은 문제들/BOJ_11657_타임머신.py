import sys

input = sys.stdin.readline
V, E = map(int, input().split())
graph = []
for _ in range(E):
    v1, v2, cost = map(int, input().split())
    graph.append((v1, v2, cost))

INF = 1e9
distance = [INF] * (V + 1)


def bellman_ford(start):
    distance[start] = 0
    for i in range(V):
        for cur_node, next_node, edge_cost in graph:
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == V - 1:
                    return True
    return False


negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    for dist in distance[2:]:
        if dist == INF:
            print("-1")
        else:
            print(dist)
