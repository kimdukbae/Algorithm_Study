import sys

input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
gas_station = list(map(int, input().split()))
gas_station.pop()

answer = distance[0] * gas_station[0]
price = gas_station[0]

for i in range(1, N - 1):
    if price > gas_station[i]:
        price = gas_station[i]
        answer += price * distance[i]
    else:
        answer += price * distance[i]

print(answer)
