# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N, Q = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(2 ** N)]
# L = list(map(int, input().split()))
# dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#
#
# def bfs():
#     count = 1
#     while q:
#         r, c = q.popleft()
#         for d in range(4):
#             nr = r + dir[d][0]
#             nc = c + dir[d][1]
#             if 0 <= nr < 2 ** N and 0 <= nc < 2 ** N and not visited[nr][nc] and A[nr][nc] != 0:
#                 count += 1
#                 q.append((nr, nc))
#                 visited[nr][nc] = True
#
#     return count
#
#
# for i in range(Q):
#     gap = 2 ** L[i]
#     for x in range(0, N, gap):
#         for y in range(0, N, gap):
#             rotate = [A[i][y:y + gap] for i in range(x, x + gap)]
#             for r in range(gap):
#                 for c in range(gap):
#                     # print((r, c), '-->', (x + c, y + gap - 1 - r))
#                     A[x + c][y + gap - 1 - r] = rotate[r][c]
#
#     for x in range(2 ** N):
#         for y in range(2 ** N):
#             cnt = 0
#             for d in range(4):
#                 nx = x + dir[d][0]
#                 ny = y + dir[d][1]
#                 if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N and A[nx][ny] != 0:
#                     cnt += 1
#             if cnt < 3 and A[x][y] > 0:
#                 A[x][y] -= 1
#
# q = deque()
# visited = [[False] * (2 ** N) for _ in range(2 ** N)]
# answer = 0
# for x in range(2 ** N):
#     for y in range(2 ** N):
#         if not visited[x][y] and A[x][y] != 0:
#             visited[x][y] = True
#             q.append((x, y))
#             answer = max(answer, bfs())
#
# for a in A:
#     print(a)
# print(sum(sum(a) for a in A))
# print(answer)
#
#


# -------------------------------------------------------------------------
# 민서님
# from collections import deque
# 
# 
# def turn(n, m, size):
#     global A
#     res = [[0] * size for _ in range(size)]
#     for i in range(size):
#         for j in range(size):
#             res[j][size - i - 1] = A[size * n + i][size * m + j]
#     for i in range(size):
#         for j in range(size):
#             A[size * n + i][size * m + j] = res[i][j]
# 
# 
# def melt():
#     global length
#     isMelt = list(list(False for _ in range(length)) for _ in range(length))
#     for x in range(length):
#         for y in range(length):
#             if A[x][y] != 0:
#                 cnt = 0
#                 for d in range(4):
#                     nx, ny = x + dx[d], y + dy[d]
#                     if 0 <= nx < length and 0 <= ny < length and A[nx][ny] != 0:
#                         cnt += 1
#                 if cnt < 3:
#                     isMelt[x][y] = True
#     for x in range(length):
#         for y in range(length):
#             if isMelt[x][y]:
#                 A[x][y] -= 1
# 
# 
# def get_biggest():
#     global length
#     max_cnt = 0
#     chk = list([False for _ in range(length)] for _ in range(length))
#     for i in range(length):
#         for j in range(length):
#             if A[i][j] != 0 and not chk[i][j]:
#                 cnt = 0
#                 que = deque()
#                 que.append([i, j])
#                 chk[i][j] = True
#                 while que:
#                     [x, y] = que.popleft()
#                     cnt += 1
#                     for d in range(4):
#                         nx, ny = x + dx[d], y + dy[d]
#                         if 0 <= nx < length and 0 <= ny < length and not chk[nx][ny] and A[nx][ny] != 0:
#                             que.append([nx, ny])
#                             chk[nx][ny] = True
#                 max_cnt = max(max_cnt, cnt)
#     return max_cnt
# 
# 
# dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# N, Q = map(int, input().split())
# length = 1 << N
# A = list(list(map(int, input().split())) for _ in range(length))
# L = list(map(int, input().split()))
# 
# for l in L:
#     cnt = 1 << (N - l)
#     size = 1 << l
#     for n in range(cnt):
#         for m in range(cnt):
#             turn(n, m, size)
#     melt()
# 
# ans = sum(sum(A[i]) for i in range(length))
# print(ans, get_biggest() if ans > 0 else 0, sep="\n")


# ---------------------------------------------
# 현우
# import sys
# from collections import deque
#
# tot = 0
# cnt = 0
# input = sys.stdin.readline
# n, q = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(2 ** n)]
# visited = [[False] * (2 ** n) for _ in range(2 ** n)]
# l = list(map(int, input().split()))
# contact = [[0] * (2 ** n) for _ in range(2 ** n)]
#
#
# def rotate(x, y, size):
#     g = [[] for _ in range(size)]
#     # 그래프 회전 후 g에 담아줌
#     for i in range(x + size - 1, x - 1, -1):
#         for j in range(y, y + size):
#             g[j - y].append(graph[i][j])
#
#     # 회전된 그래프를 원래 그래프에 담아줌
#     for i in range(x, x + size):
#         for j in range(y, y + size):
#             graph[i][j] = g[i - x][j - y]
#
#
# # bfs로 외부 접촉 계산
# # 얼음 녹이기
# def bfs(x, y):
#     global n, visited, contact
#     q = deque()
#     dx = -1, 0, 1, 0
#     dy = 0, 1, 0, -1
#     q.append((x, y))
#     visited[x][y] = True
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 범위 밖일 때, 접촉 + 1
#             if nx >= len(graph) or nx < 0 or ny >= len(graph) or ny < 0:
#                 contact[x][y] += 1
#             # 얼음이 아닐 때, 접촉 + 1
#             elif graph[nx][ny] <= 0:
#                 contact[x][y] += 1
#             else:
#                 visited[x][y] = True
#                 q.append((nx, ny))
#
#
# def find_bfs(x, y):
#     dx = -1, 0, 1, 0
#     dy = 0, 1, 0, -1
#     q = deque()
#     answer = 1
#     q.append((x, y))
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < len(graph) and 0 <= ny < len(graph) and not visited[nx][ny]:
#                 if graph[nx][ny] > 0:
#                     answer += 1
#                     visited[nx][ny] = True
#                     q.append((nx, ny))
#     return answer
#
#
# for x in l:
#     # 1. 회전
#     for a in range(0, len(graph), 2 ** x):
#         for b in range(0, len(graph), 2 ** x):
#             rotate(a, b, 2 ** x)
#     for g in graph:
#         print(*g)
#     print()
#     # 2. 초기화
#     contact = [[0] * (2 ** n) for _ in range(2 ** n)]
#     visited = [[False] * (2 ** n) for _ in range(2 ** n)]
#     # 3. bfs로 융해 될 얼음 찾기
#     for a in range(len(graph)):
#         for b in range(len(graph)):
#             if graph[a][b] > 0 and not visited[a][b]:
#                 bfs(a, b)
#     # 4. 융해
#     for i in range(len(graph)):
#         for j in range(len(graph)):
#             # 2번 이상 외부 접촉시 -1
#             if contact[i][j] >= 2 and graph[i][j] > 0:
#                 graph[i][j] -= 1
#
# visited = [[False] * (2 ** n) for _ in range(2 ** n)]
# ans = []
# for i in range(len(graph)):
#     for j in range(len(graph)):
#         if graph[i][j] > 0:
#             tot += graph[i][j]
#             if not visited[i][j]:
#                 visited[i][j] = True
#                 ans.append(find_bfs(i, j))
# print(tot)
# if ans:
#     print(max(ans))
# else:
#     print(0)
