import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # --> 꺼낸 노드 = 현재 최소 비용을 갖는 노드
        # 해당 노드의 비용이 현재 distance 배열에 기록된 비용보다 크다면 최단 경로가 아니기 때문에 무시해도 상관 X

        # 만약 이 조건을 생략하게 된다면 이미 방문한 정점을 중복하여 탐색하게 됨.
        # 그렇다면 큐에 있는 모든 다음 노드에 대한 인접노드에 대한 탐색을 다시 진행하게 된다.
        # 또한, 주어진 그래프가 완전 그래프이고 이 조건이 없다면 시간 복잡도는 O(E ** 2)으로 가게 되어 효율성 떨어진다.
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# sample input
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
