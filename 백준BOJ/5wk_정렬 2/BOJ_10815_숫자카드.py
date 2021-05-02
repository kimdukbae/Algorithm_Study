# import sys
#
# input = sys.stdin.readline
# N = int(input())
# sang_card = list(map(int, input().split()))
# M = int(input())
# check = list(map(int, input().split()))
#
# sang_card.sort()
# check2 = sorted(check)
#
# # print(sang_card)
# # print(check2)
#
# sang_idx, check_idx = 0, 0
# answer = []
# while sang_idx < len(sang_card) or check_idx < len(check2):
#     if sang_card[sang_idx] == check2[check_idx]:
#         answer.append(sang_card[sang_idx])
#         sang_idx += 1
#         check_idx += 1
#     elif sang_card[sang_idx] > check2[check_idx]:
#         check_idx += 1
#     else:
#         sang_idx += 1
#
# for chk in check:
#     if chk in answer:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

import sys

input = sys.stdin.readline
N = int(input())
card = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

# 이분 탐색을 위한 오름차순 정렬
card.sort()

answer = [0] * M
# 이분 탐색 진행
for i in range(M):
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if card[mid] == check[i]:
            answer[i] = 1
            break
        elif card[mid] < check[i]:
            left = mid + 1
        else:
            right = mid - 1

print(*answer)
