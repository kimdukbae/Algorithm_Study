# import sys
#
# input = sys.stdin.readline
# N = int(input())
# dice = list(map(int, input().split()))
# ans = 0

# if N == 1:
#     ans = dice[0] + dice[1] + dice[2] + dice[3] + dice[4] + dice[5]
# elif N == 2:
#     ans = ((dice[0] * N * N) + (dice[1] * N * 2) + (dice[2] * N)) * N
# else:
#     ans = ((dice[0] * N * N) + (dice[1] * N * 2) + (dice[2] * N)) * (N - 1) + (dice[0] * N * 3 * (N - 2))
#
# print(ans)


# 2
import sys

input = sys.stdin.readline
N = int(input())
dice = list(map(int, input().split()))
temp = []
ans = 0

if N == 1:
    temp = sorted(dice)
    for i in range(len(temp) - 1):
        ans += temp[i]

else:
    # [A-F 중 최솟값] [B-E 중 최솟값] [C-D 중 최솟값] 구한 후 배열에 저장
    temp.append(min(dice[0], dice[5]))
    temp.append(min(dice[1], dice[4]))
    temp.append(min(dice[2], dice[3]))
    temp.sort()     # 최솟값을 구하기 위해서 오름차순 정렬

    # 보이는 면의 개수에 따른 최솟값 계산 (위 temp 리스트를 정렬한 이유)
    one = temp[0]
    two = temp[0] + temp[1]
    three = temp[0] + temp[1] + temp[2]

    face1 = (4 * (N - 1) * (N - 2)) + ((N - 2) ** 2)
    face2 = 4 * (N - 1) + 4 * (N - 2)

    ans += (one * face1) + (two * face2) + (three * 4)

print(ans)
