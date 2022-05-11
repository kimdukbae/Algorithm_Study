import sys

input = sys.stdin.readline

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(int(input()))

coin = [25, 10, 5, 1]
for i in range(len(test_cases)):
    change = test_cases[i]
    answer = []
    for j in range(len(coin)):
        answer.append(change // coin[j])
        change %= coin[j]
    print(*answer)
