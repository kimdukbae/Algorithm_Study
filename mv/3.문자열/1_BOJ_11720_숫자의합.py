import sys

input = sys.stdin.readline

N = int(input())
numbers = input()

answer = 0
for i in range(N):
    answer += int(numbers[i])

print(answer)
