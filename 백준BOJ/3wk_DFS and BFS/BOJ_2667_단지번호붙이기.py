# BFS
# visited 배열 안쓰고 1을 지우는 방식도 ㄱㅊ을듯!!
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
plan = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque([])
total = 0
house_complex = []


# 1인 것부터 탐색하기 때문에 home = 1로 초기화
# bfs() 호출할 시 1개의 단지 안에 속하는 집의 수를 구해주게 된다.
def bfs():
    home = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dir[i][0]
            nc = c + dir[i][1]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and plan[nr][nc] == 1:
                visited[nr][nc] = True
                q.append((nr, nc))
                home += 1
    house_complex.append(home)


for i in range(N):
    for j in range(N):
        # 백준 예제에서는 총 3번 BFS() 함수 호출된다고 생각하면 쉽다. (전체 단지 덩어리 수)
        if not visited[i][j] and plan[i][j] == 1:
            q.append((i, j))
            visited[i][j] = True
            total += 1
            bfs()

house_complex.sort()
# print(len(house_complex))
print(total)

for hc in house_complex:
    print(hc)
