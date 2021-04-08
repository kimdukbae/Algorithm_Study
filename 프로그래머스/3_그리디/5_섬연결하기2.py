# 섬과 섬 연결하기
def union(parent, a, b):
    A = find(parent, a)
    B = find(parent, b)

    if A < B:
        parent[B] = A
    else:
        parent[A] = B


# 섬에 사이클 생기는지 판단
def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def solution(n, costs):
    parents = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[2])

    answer = 0
    while costs:
        city1, city2, cost = costs.pop(0)
        if find(parents, city1) != find(parents, city2):
            union(parents, city1, city2)
            answer += cost

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
print(solution(6, [[1, 4, 1], [0, 3, 2], [1, 2, 2], [0, 4, 3], [2, 5, 3], [4, 5, 4], [0, 1, 5], [3, 4, 10]]))
