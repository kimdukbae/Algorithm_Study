import sys

# 시간초과 발생으로 인해 recursion 조정
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())
graph = [[0, []] for _ in range(N + 1)]
for i in range(2, N + 1):
    animal, animal_cnt, island = input().split()
    if animal == 'W':
        animal_cnt = -int(animal_cnt)
    graph[i][0] = int(animal_cnt)
    graph[int(island)][1].append(i)


# print(graph)


def dfs(depth):
    # 늑대 or 양 마리 수 저장 및 갱신
    answer = graph[depth][0]
    for g in graph[depth][1]:
        answer += dfs(g)

    # 섬을 이동할 때 섬에 늑대만 있거나 양보다 늑대가 많아서 양을 다 잡아 먹을 때
    if answer < 0:
        return 0
    else:
        return answer


print(dfs(1))
