import sys

input = sys.stdin.readline
K = int(input())
RED, BLUE = 1, -1
sys.setrecursionlimit(10 ** 6)
# 백준에서 재귀의 깊이 제한이 1000 이라고 함.
# 재귀 제한을 설정해주지 않으면 recursionError 가 발생함. 따라서 재귀 제한을 설정해줬음.


def dfs(vertex, color):
    global flag
    colors[vertex] = color  # 시작 정점 color 색으로 칠함.
    
    # 인접한 정점들 중에서
    for graph in graphs[vertex]:
        # 인접한 정점의 색상이 같으면 이분 그래프 X 이므로 종료
        if colors[graph] == color:
            flag = False
            return
        # 정점을 칠한적이 없으면 재귀 함수 호출
        if colors[graph] == 0:
            dfs(graph, -color)


for i in range(K):
    V, E = map(int, input().split())

    graphs = [[] for _ in range(V + 1)]   # 연결리스트 그래프
    colors = [0] * (V + 1)   # 색상 저장
    flag = True
    for _ in range(E):
        x, y = map(int, input().split())
        graphs[x].append(y)
        graphs[y].append(x)

    for v in range(1, V + 1):
        if not flag:
            break
        if colors[v] == 0:
            dfs(v, RED)   # 처음에 빨간색으로 칠함. (파란색으로 먼저 칠해도 상관 X)

    print('YES' if flag else "NO")
