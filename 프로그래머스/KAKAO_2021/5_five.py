# SELECT A.ID1, COUNT(*)
# FROM (SELECT ID1 FROM FRIENDS
#       UNION ALL
#       SELECT ID2 FROM FRIENDS) AS A
# GROUP BY A.ID1
# ORDER BY A.ID1;


maps = [
    [9, 8, 17, 55, 19, 7],
    [1, 25, 5, 39, 28, 8],
    [88, 19, 28, 3, 2, 9],
    [76, 73, 7, 18, 16, 14],
    [99, 8, 8, 7, 11, 9],
    [1, 18, 4, 10, 3, 6],
]
p = 16
r = 4
n = 6


def dfs(depth, x, y, goal, dir, p, r, n, visited, maps):
    dx = -1, 0, 1, 0
    dy = 0, 1, 0, -1
    tot = 0
    if depth == goal:
        if maps[x][y] < p / 2:
            return 1
        return 0
    if maps[x][y] <= p:
        tot += 1
    for i in range(dir, dir + 2):
        nx = x + dx[i] if i < 4 else x + dx[i - 4]
        ny = y + dy[i] if i < 4 else y + dy[i - 4]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True

            tot += dfs(depth + 1, nx, ny, goal, dir, p, r, n, visited, maps)
    return tot


ddx = -1, 0, 0, -1
ddy = 0, 0, -1, -1
answer = 0
n = len(maps)
visited = [[False] * n for _ in range(n)]
#
for i in range(n + 1):
    for j in range(n + 1):
        tot = 0
        visited = [[False] * n for _ in range(n)]
        for k in range(4):
            nnx = i + ddx[k]
            nny = j + ddy[k]
            if 0 <= nnx < n and 0 <= nny < n:
                visited[nnx][nny] = True
                tot += dfs(0, nnx, nny, r // 2 - 1, k, p, r, n, visited, maps)
        answer = max(answer, tot)
print(answer)

