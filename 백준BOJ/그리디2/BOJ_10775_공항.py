import sys

# 비행기를 도킹할 때 항상 넣을 수 있는 가장 큰 수의 게이트에 도킹해야함. (최대 도킹 수를 구해야하므로)
input = sys.stdin.readline
G = int(input())
P = int(input())
docking = list(int(input()) for _ in range(P))
parents = [i for i in range(G + 1)]
ans = 0


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]  # 경로압축
    # return find(parent, parent[x])  # 일반적인 find 구현
    # BOJ 재귀 깊이 1,000


def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


for d in docking:
    root = find(parents, d)
    # 0일 때 끝나는 이유 -> 비행기가 어느 게이트에도 도킹할 수 없으면 공항 폐쇄되고,
    # 이후 어떤 비행기도 도착할 수 없기 때문에 더이상 탐색할 필요가 X
    if root == 0:
        break

    # union(parents, d, d - 1) --> (Ex) 2-3 연결되어있고 1은 비어있음. d=3이면 1-2-3 연결되어야 하는데
    # 3의 부모인 2와 1을 연결해야하는데, 위 코드는 3과 2를 연결해서 오류발생!
    union(parents, root, root - 1)
    ans += 1

print(ans)
