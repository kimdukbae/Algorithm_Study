'''
# 1. 순열 (제일 먼저 생각한 방법)
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
op = list(map(int, input().split()))

op_list = ['+', '-', '*', '/']
op_select = []

for i in range(len(op)):
    for j in range(op[i]):
        op_select.append(op_list[i])

maximum = -1e9
minimum = 1e9

for case in permutations(op_select, N - 1):
    total = number[0]
    for x in range(1, N):
        if case[x - 1] == '+':
            total += number[x]
        elif case[x - 1] == '-':
            total -= number[x]
        elif case[x - 1] == '*':
            total *= number[x]
        elif case[x - 1] == '/':
            total = int(total / number[x])

    if total > maximum:
        maximum = total

    if total < minimum:
        minimum = total

print(maximum)
print(minimum)
'''

# 2. 백트래킹
import sys

input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum

    if depth == N:
        if total > maximum:
            maximum = total
        if total < minimum:
            minimum = total
        return

    if plus > 0:
        dfs(depth + 1, total + number[depth], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(depth + 1, total - number[depth], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(depth + 1, total * number[depth], plus, minus, multiply - 1, divide)
    if divide > 0:
        dfs(depth + 1, int(total / number[depth]), plus, minus, multiply, divide - 1)


dfs(1, number[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
