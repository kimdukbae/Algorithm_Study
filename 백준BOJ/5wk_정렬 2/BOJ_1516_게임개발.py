import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
cost = [0] * (N + 1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))[:-1]
    cost[i] = data[0]
    for j in data[1:]:
        graph[j].append(i)
        indegree[i] += 1

# print(graph)
# print(indegree)
# print(cost)

# 위상 정렬
q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

answer = [0] * (N + 1)
while q:
    now = q.popleft()
    answer[now] += cost[now]
    for g in graph[now]:
        indegree[g] -= 1
        answer[g] = max(answer[g], answer[now])
        if indegree[g] == 0:
            q.append(g)

for i in range(1, N + 1):
    print(answer[i])
