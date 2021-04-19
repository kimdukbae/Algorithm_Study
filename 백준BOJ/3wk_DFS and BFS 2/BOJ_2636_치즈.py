import sys
from collections import deque

input = sys.stdin.readline
row, col = map(int, input().split())
cheese_board = [list(map(int, input().split())) for _ in range(row)]

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans_list = []


def bfs():
    visited = [[False] * col for _ in range(row)]
    q = deque([(0, 0)])
    visited[0][0] = True
    cheese_cnt = 0  # 1시간 마다 녹는 치즈의 개수 저장

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                # 치즈부터 찾는 것이 아닌 공기부터 찾는다.
                # 치즈부터 찾지않고 공기부터 찾게되면 치즈의 구멍은 건드리지 않게 된다.
                if cheese_board[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True

                # 가장자리 치즈를 녹인다.
                elif cheese_board[nx][ny] == 1:
                    visited[nx][ny] = True
                    cheese_board[nx][ny] = 0
                    cheese_cnt += 1

    # for c in cheese_board:
    #     print(*c)
    # print()

    ans_list.append(cheese_cnt)
    return cheese_cnt


while True:
    cnt = bfs()
    # 여기서 all(), any() 함수 어떻게 쓰는지
    # 2차원 배열의 모든 원소가 0일 때 종료 (치즈 전부 녹았을 때)
    if cnt == 0:
        print(len(ans_list) - 1)
        print(ans_list[-2])
        break
