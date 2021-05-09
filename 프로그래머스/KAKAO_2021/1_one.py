def solution(s):
    answer = ''
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    temp = ''

    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
            temp = ''
        else:
            temp += s[i]
            if temp in words:
                answer += str(words.index(temp))
                temp = ''

    return int(answer)


print(solution("23four5six7"))
