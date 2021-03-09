import sys

N = sys.stdin.readline().strip()
answer = []
num = 0

for x in N:
    if x.isalpha():
        answer.append(x)

    else:
        num += int(x)

answer.sort()

if num != 0:
    answer.append(str(num))

print(''.join(answer))