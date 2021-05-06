import sys

input = sys.stdin.readline
string = input().rstrip()
bomb = input().rstrip()
stack = []


for i in range(len(string)):
    stack.append(string[i])
    # stack[-x:] -> 문자열의 오른쪽에서부터 x번째 ~ 마지막 까지 잘라낸다.
    # 문자열 인덱스 슬라이싱 활용을 잘하자!
    if stack[-1] == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')
