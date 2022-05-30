import sys

input = sys.stdin.readline

words = input().rstrip()
bomb = input().rstrip()


def solution(arg_words, arg_bomb):
    answer = ""
    stack = []

    for i in range(len(arg_words)):
        stack.append(arg_words[i])
        if stack[-1] == arg_bomb[-1] and "".join(stack[-len(arg_bomb):]) == arg_bomb:
            del stack[-len(arg_bomb):]

    if stack:
        answer = "".join(stack)
    else:
        answer = "FRULA"

    return answer


print(solution(words, bomb))
