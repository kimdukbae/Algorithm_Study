import sys

input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]
empty = [(x, y) for x in range(9) for y in range(9) if sudoku[x][y] == 0]


def select_num(x, y):
    numbers = [i + 1 for i in range(9)]

    for i in range(9):
        if sudoku[x][i] in numbers:
            numbers.remove(sudoku[x][i])
        if sudoku[i][y] in numbers:
            numbers.remove(sudoku[i][y])

    x1, y1 = (x // 3) * 3, (y // 3) * 3
    for r in range(x1, x1 + 3):
        for c in range(y1, y1 + 3):
            if sudoku[r][c] in numbers:
                numbers.remove(sudoku[r][c])

    return numbers


flag = False


def dfs(depth):
    global flag

    if flag:
        return
    if depth == len(empty):
        for s in sudoku:
            print(*s)
        flag = True
        return

    r, c = empty[depth]
    cases = select_num(r, c)

    for case in cases:
        sudoku[r][c] = case
        dfs(depth + 1)
        sudoku[r][c] = 0


dfs(0)
# 랭퍼든 / 사다리조작 / 스도쿠
