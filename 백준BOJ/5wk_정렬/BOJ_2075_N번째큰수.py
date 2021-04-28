# Python3 메모리 초과 / PyPy3 통과!
import sys
import heapq

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

q = []
# 우선순위 큐에 먼저 첫 번째 행의 원소들을 넣어준다.
for b in board[0]:
    heapq.heappush(q, b)

# 2번째 행부터 마지막 행까지 상위 N개의 수를 계속 갱신한다.
for i in range(1, N):
    for b in board[i]:
        if q[0] < b:
            heapq.heappush(q, b)
            heapq.heappop(q)

print(q[0])
