import sys

input = sys.stdin.readline

N = int(input())

chess = [0] * N
answer = 0


# 해당 row에서 어떤 열에 놓아야 서로 공격하지 않게 배치하도록 처리
def checkQueen(row):
    for x in range(row):
        # 같은 열에 있는지 체크 or 왼쪽, 오른쪽 대각선에 다른 퀸이 있는 경우 체크
        if chess[row] == chess[x] or abs(chess[row] - chess[x]) == abs(row - x):
            return False

    return True


def backtracking(depth):
    global answer

    if depth == N:
        answer += 1
        return

    # depth는 행, y는 열
    # 즉, 각 행마다 열에 체스 배치해보는 작업
    for y in range(N):
        chess[depth] = y
        if checkQueen(depth):
            backtracking(depth + 1)


backtracking(0)
print(answer)

'''
import sys

input = sys.stdin.readline

N = int(input())

a = [0] * N
b = [0] * (2 * N - 1)
c = [0] * (2 * N - 1)
answer = 0


def dfs(depth):
    global answer

    if depth == N:
        answer += 1
        return

    for i in range(N):
        if not a[i] and not b[depth + i] and not c[depth - i + N - 1]:
            a[i] = b[depth + i] = c[depth - i + N - 1] = 1
            dfs(depth + 1)
            a[i] = b[depth + i] = c[depth - i + N - 1] = 0


dfs(0)
print(answer)
'''
