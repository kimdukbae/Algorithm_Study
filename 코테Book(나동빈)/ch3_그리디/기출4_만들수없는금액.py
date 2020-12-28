N = int(input())
coin = list(map(int, input().split()))
coin.sort()

# 왜 target 보다 현재 코인이 크면 만들 수 없는 금액이라 하는걸까...
target = 1
for i in coin:
    if target < i:
        break
    target += i

print(target)