import sys

input = sys.stdin.readline

N = int(input())
dice = list(map(int, input().split()))

answer = 0

if N == 1:
    temp = sorted(dice)
    for i in range(5):
        answer += temp[i]
    print(answer)

else:
    temp = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
    temp.sort()

    one = temp[0]
    two = temp[0] + temp[1]
    three = temp[0] + temp[1] + temp[2]

    answer = one * (4 * (N - 1) * (N - 2) + (N - 2) * (N - 2))
    answer += two * (4 * (N - 1) + 4 * (N - 2))
    answer += three * 4

    print(answer)
