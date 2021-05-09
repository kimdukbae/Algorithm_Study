# 9:46
import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
dx = -1, -1, 0, 1, 1, 1, 0, -1
dy = 0, 1, 1, 1, 0, -1, -1, -1
graph = [[[] for _ in range(N)] for _ in range(N)]
q = deque()
over_two = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    # graph에 [질량, 속도, 방향] 삽입
    graph[r - 1][c - 1].append([m, s, d])
    q.append([r - 1, c - 1, m, s, d])

# 맵 벗어나면 반대편으로 이동
def switch(x, y, s, d):
    nx = x + dx[d] * (s % N)
    ny = y + dy[d] * (s % N)
    if nx < 0:
        nx += N
    if ny < 0:
        ny += N
    if nx >= N:
        nx -= N
    if ny >= N:
        ny -= N
    return (nx, ny)


def move(size):
    for _ in range(size):
        x, y, m, s, d = q.popleft()  # x, y, 질량, 속도, 방향 꺼냄
        # 방향대로 이동. 단, 맵을 벗어날 시 반대편 방향으로 이동
        nx, ny = switch(x, y, s, d)
        # 원래 있던 자리에서 새로운 자리로
        graph[x][y].pop(0)
        graph[nx][ny].append([m, s, d])


def division(x, y):
    tot_m = tot_s = 0  # 총 질량, 스피드
    flag = True  # 합쳐지는 파볼의 방향이 모두 같으면 True.
    direct = graph[x][y][0][2] % 2  # 기준 방향. 합쳐지는 파이어볼의 방향이 모두 이 방향을 따르면 0,2,4,6
    for mass, speed, di in graph[x][y]:
        # 질량 스피드 모두 더함
        tot_m += mass
        tot_s += speed
        # 방향 검사
        if direct != di % 2:
            flag = False
    each_m = tot_m // 5
    each_s = tot_s // len(graph[x][y])
    graph[x][y] = []
    if each_m > 0:  # 질량이 0이면 소멸한다.
        if flag:  # 방향이 모두 같을 때
            for i in range(0, 8, 2):
                graph[x][y].append([each_m, each_s, i])
        else:  # 방향이 제각각일때
            for i in range(1, 8, 2):
                graph[x][y].append([each_m, each_s, i])


time = 0
while q and time < K:
    # 맵에 있는 파이어볼 모두 이동
    size = len(q)
    move(size)
    # 이동이 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    # 파이어볼이 나누어진 이후에도 2개 이상의 파이어볼이 존재하면?
    # 어떡하지? -> 파이어볼이 4개로 나눠진다음 흩어지는게 아님.
    # 그냥 그자리에 4개 생성되고 가만히 있는 것임;

    # 맵을 검사해서 중첩된 파이어볼을 찾는다.
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) >= 2:
                division(i, j)

    # 맵을 검사해서 파이어볼을 큐에 다 담아준다.
    for i in range(N):
        for j in range(N):
            for m, s, d in graph[i][j]:
                q.append([i, j, m, s, d])
    time += 1
answer = 0
for i in range(N):
    for j in range(N):
        for m, _, _ in graph[i][j]:
            answer += m
print(answer)