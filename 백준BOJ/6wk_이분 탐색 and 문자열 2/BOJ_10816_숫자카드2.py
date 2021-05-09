# 이분 탐색으로 풀면 --> 중복된 거 있으면 (가장 마지막의 원소의 인덱스 - 맨 처음 원소의 인덱스) 반환
import sys
import collections

input = sys.stdin.readline
N = int(input())
sang_card = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

counter = collections.Counter(sang_card)

answer = []
for chk in check:
    if counter[chk] > 0:
        answer.append(counter[chk])
    else:
        answer.append(0)

print(*answer)
