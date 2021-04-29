# 왜 틀린지 모르겠음...
#
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# crane_limit = list(map(int, input().split()))
# M = int(input())
# boxes = list(map(int, input().split()))
#
# crane_limit.sort(reverse=True)
# boxes.sort(reverse=True)
# size, ans = 0, 0
#
# if boxes[0] > crane_limit[0]:
#     print(-1)
#     sys.exit(0)
# else:
#     크레인이 무조건 내가 구해준 size만큼 돌라는 보장이 없음
#     (반례) crane : 2 1
#            box : 2 2 2 2 1
#     if M % N == 0:
#         size = M // N
#     else:
#         size = M // N + 1
#
#     while size > 0:
#         ans += 1
#         for i in range(N):
#             for j in range(M):
#                 if boxes[j] <= crane_limit[i] and boxes[j] != 0:
#                     boxes[j] = 0
#                     break
#         size -= 1
#
# print(ans)


import sys

input = sys.stdin.readline
N = int(input())
crane_limit = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

# crane의 무게제한에 맞춰 가장 최적의 box를 옮긴다.
# 즉, (crane 무게제한 - box 무게) 가장 최소가 되도록 crane으로 box를 옮긴다.
# --> 그러기 위해서는 내림차순 정렬한다. 내림차순 정렬을 해주었기 때문에 이렇게 고를 수 있다.
crane_limit.sort(reverse=True)
boxes.sort(reverse=True)

# 내림차순 정렬 후 가장 큰 무게의 box가 가장 큰 crane 무게제한보다 크면
# 모든 박스를 배로 옮길 수 없다고 판단!
if boxes[0] > crane_limit[0]:
    print(-1)
    sys.exit(0)

# crane이 옮긴 box가 몇 번째인지 저장하는 리스트
# (Ex)
# crane[0] = 1 -> (0+1)번 crane은 직전에 0번 box를 옮김
# crane[1] = 4 -> (1+1)번 crane은 직전에 3번 box를 옮김
# crane[2] = 5 -> (2+1)번 crane은 직전에 4번 box를 옮김
position = [0] * N

# 옮긴 박스를 방문처리 해주기 위한 리스트
visited = [False] * M
count, ans = 0, 0

while True:
    # 모든 box 다 옮겼으면 종료
    if count == len(boxes):
        break
    # 모든 crane을 동시에 움직이는데
    for i in range(N):
        # crane이 "position[i]번째 box(직전에 (position[i] - 1)번째 box를 골랐으므로 position[i]번째 부터) ~ 마지막 box까지"
        # 탐색하도록 하는 while문
        while position[i] < len(boxes):
            # box를 crane으로 아직 안 옮겼고, 무게 제한보다 가벼운 box를 crane으로 옮길 수 있다면
            if not visited[position[i]] and boxes[position[i]] <= crane_limit[i]:
                visited[position[i]] = True
                position[i] += 1  # position[i]의 value는 옮긴 박스의 번호 + 1
                count += 1  # 옮긴 box 개수 + 1
                break
            # 조건 만족 못하면 다음 box를 해당 crane으로 옮길 수 있는지 탐색하기 위한 증가
            position[i] += 1
    ans += 1

print(ans)

