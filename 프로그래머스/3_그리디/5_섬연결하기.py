# https://velog.io/@ckstn0778/%EC%84%AC-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0-O-1

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


def solution(n, costs):
    parent = [i for i in range(n)]
    edge = []

    for cost in costs:
        edge.append((cost[2], cost[0], cost[1]))

    edge.sort(reverse=True)

    result = 0
    while edge:
        cost, a, b = edge.pop()

        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost

    return result

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
