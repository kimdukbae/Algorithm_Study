import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    d = input().rstrip()[1:-1].split(",")
    q = deque(d)

    reverse_cnt = 0
    error_flag = True

    if n <= 0:
        q = []

    for cmd in p:
        if cmd == 'R':
            reverse_cnt += 1
        elif cmd == 'D':
            if len(q) <= 0:
                error_flag = False
                print("error")
                break
            else:
                if reverse_cnt % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if error_flag:
        if reverse_cnt % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
