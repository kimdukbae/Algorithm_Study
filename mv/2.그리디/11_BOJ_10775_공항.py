import sys

input = sys.stdin.readline

G = int(input())
P = int(input())
docking = []
for _ in range(P):
    docking.append(int(input()))

node = [i for i in range(G + 1)]
answer = 0


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


for dock in docking:
    root = find(node, dock)

    if root == 0:
        break

    union(node, root, root - 1)
    answer += 1

print(answer)
