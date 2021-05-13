import sys

input = sys.stdin.readline


# 이해 살짝 안됨
def bellman_ford():
    # 모든 정점에 대해
    for start in range(1, V + 1):
        # 벨만-포드 수행
        for i in range(1, V + 1):
            for next_node, edge_time in graph[i]:
                if distance[next_node] > distance[i] + edge_time:
                    distance[next_node] = distance[i] + edge_time
                    # 한 정점에서 출발했을 때 음수 간선 순환있으면 True로 종료
                    if start == V:
                        return True

    return False


TC = int(input())
for _ in range(TC):
    V, E, W = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2, time = map(int, input().split())
        graph[v1].append((v2, time))
        graph[v2].append((v1, time))
    for _ in range(W):
        v1, v2, time = map(int, input().split())
        graph[v1].append((v2, -time))

    INF = 1e9
    distance = [INF] * (V + 1)
    time_travel_possible = bellman_ford()

    # 음수 간선 순환이 있어야 시간 되돌아오는 여행 가능한다고 판단
    if time_travel_possible:
        print("YES")
    else:
        print("NO")
