# PyPy3, Python3 --> visited 배열 없이는 메모리 초과
# --> 그래서 visited 배열 생성 후에는 시간 초과
import sys
from collections import deque

# .zfill()
input = sys.stdin.readline
T = int(input())


def bfs(start, end, visited):
    q = deque([('', start)])
    visited[start] = True

    while q:
        command, cur = q.popleft()
        if cur == end:
            return command

        computation = (cur * 2) % 10000
        if not visited[computation]:
            visited[computation] = True
            q.append((command + 'D', computation))

        # n=0 이라면 n-1은 -1이다.
        # -1 mod 10000 = 9999 로 visited[9999]가 True 된다. --> 조건식 하나로도 충분
        computation = (cur - 1) % 10000
        if not visited[computation]:
            visited[computation] = True
            q.append((command + 'S', computation))

        computation = (cur % 1000) * 10 + cur // 1000
        if not visited[computation]:
            visited[computation] = True
            q.append((command + 'L', computation))

        computation = (cur % 10) * 1000 + cur // 10
        if not visited[computation]:
            visited[computation] = True
            q.append((command + "R", computation))


for _ in range(T):
    initial, final = map(int, input().split())
    visited = [False] * 10000

    print(bfs(initial, final, visited))

# cur = 1
# print((cur % 1000) * 10 + cur // 1000)
# print((cur % 10) * 1000 + cur // 10)

# now = 1
# l_now = len(str(now))
#
# if l_now != 4:
#     t = now * 10
#     print(t)
# else:
#     t, d = divmod(now, 10 ** (l_now - 1))
#     t += (d * 10)
#     print(t)
#
# if l_now == 1:
#     t = now * 1000
#     print(t)
# else:
#     t, d = divmod(now, 10)
#     t += (d * 1000)
#     print(t)
