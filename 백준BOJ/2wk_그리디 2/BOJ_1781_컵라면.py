import sys
import heapq

input = sys.stdin.readline
N = int(input())
problems = [list(map(int, input().split())) for _ in range(N)]
problems.sort()

explore = []

for problem in problems:
    # 일단 문제 풀어본다.
    heapq.heappush(explore, problem[1])

    # 데드라인이 같은 문제를 풀었을 때 컵라면 최대로 받을 수 있는 문제만 풀도록 함.
    if problem[0] < len(explore):
        heapq.heappop(explore)  # Min Heap 으로 오름차순 / 제일 작은 컵라면 문제 제거

print(sum(explore))
