import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

sensors = list(map(int, input().split()))

sensors.sort()

answer = []

if K >= N:
    print(0)
else:
    for i in range(N - 1):
        answer.append(abs(sensors[i] - sensors[i + 1]))

    answer.sort()

    for _ in range(K - 1):
        answer.pop()

    print(sum(answer))
