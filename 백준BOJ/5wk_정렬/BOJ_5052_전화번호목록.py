import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    phone_num = [input() for _ in range(N)]

    phone_num.sort()
    flag = False
    basis = ''
    for i in range(N):
        if not flag:
            basis = phone_num.pop(0)
        if phone_num:
            for pn in phone_num:
                if basis == pn[0:len(basis)]:
                    flag = True
                    break

    if flag:
        print('NO')
    else:
        print('YES')
