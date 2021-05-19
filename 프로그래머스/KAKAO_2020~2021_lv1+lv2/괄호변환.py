def divide(word):
    open_bracket, close_bracket = 0, 0
    for i in range(len(word)):
        if word[i] == '(':
            open_bracket += 1
        elif word[i] == ')':
            close_bracket += 1
        if open_bracket == close_bracket:
            return word[:i + 1], word[i + 1:]


def is_valid_string(word):
    stack = []
    for i in range(len(word)):
        if word[i] == '(':
            stack.append(word[i])
        else:
            if stack:
                stack.pop()
    if stack:
        return False
    else:
        return True


def solution(p):
    # 1번
    if not p:
        return p

    # 2번
    u, v = divide(p)

    # 3번
    if is_valid_string(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        if u:
            u = u.replace(u[0], "")
        if u:
            u = u.replace(u[-1], "")
        for i in range(len(u)):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('

        return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
