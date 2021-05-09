# 행 개수 n / 선택된 행의 위치 k / 수행한 명령어들 cmd
def solution(n, k, cmd):
    answer = ''
    original = [i for i in range(n)]
    board = [i for i in range(n)]
    stack = []
    pointer = k

    for i in range(len(cmd)):
        command = cmd[i]
        if command[0] == 'U':
            pointer -= int(command[2])
        elif command[0] == 'D':
            pointer += int(command[2])
        elif command[0] == 'C':
            stack.append(board[pointer])
            del board[pointer]
            if pointer >= len(board):
                pointer -= 1
        elif command[0] == 'Z':
            data = stack.pop()
            board.insert(data, data)
            if pointer > data:
                pointer += 1

    for ori in original:
        if ori in board:
            answer += 'O'
        else:
            answer += 'X'

    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
