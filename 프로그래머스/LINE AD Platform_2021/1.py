def solution(inputString):
    answer = 0
    stack = []
    for i in range(len(inputString)):
        stack.append([i, inputString[i]])

    for i in range(len(inputString) - 1, -1, -1):
        if stack[i][1] not in ['(', ')', '{', '}', '[', ']', '<', '>']:
            del stack[i]

    check = []
    for i in range(len(stack) - 1, -1, -1):
        if stack[i][1] == ')' or stack[i][1] == '}' or stack[i][1] == ']' or stack[i][1] == '>':
            check.append(stack[i])
            del stack[i]

    # print(stack)
    # print(check)

    if not stack and check:
        if check[-1][1] == ')' or check[-1][1] == '}' or check[-1][1] == ']' or check[-1][1] == '>':
            return 0

    count, idx = 0, 0
    while check:
        basis = check[-1]
        if basis[1] == '>' and stack[-1][1] == '<' and basis[0] > stack[-1][0]:
            idx = basis[0]
            check.pop()
            stack.pop()
        elif basis[1] == ')' and stack[-1][1] == '(' and basis[0] > stack[-1][0]:
            idx = basis[0]
            check.pop()
            stack.pop()
        elif basis[1] == ']' and stack[-1][1] == '[' and basis[0] > stack[-1][0]:
            idx = basis[0]
            check.pop()
            stack.pop()
        elif basis[1] == '}' and stack[-1][1] == '{' and basis[0] > stack[-1][0]:
            idx = basis[0]
            check.pop()
            stack.pop()
        else:
            answer = -(basis[0])
            return answer
        count += 1

    if stack:
        answer = -idx
        return answer

    answer = count
    return answer


print(solution('Hello, world!'))
print(solution('line [({<plus>)}]'))
print(solution('line [({<plus>})'))
print(solution('>_<'))
print(solution('x * (y + z) ^ 2 = ?'))
