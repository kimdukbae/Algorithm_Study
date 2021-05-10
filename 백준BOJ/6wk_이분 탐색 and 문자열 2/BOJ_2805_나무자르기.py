# M이 20억이어서 그런가... 
# Python3 시간 초과 / PyPy3만 통과 -> 왜 그런지 모르겠음
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 1
right = max(trees)
answer = 0
while left <= right:
    mid = (left + right) // 2
    total = 0
    for tree in trees:
        if mid <= tree:
            total += tree - mid

    if total >= M:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)
