def solution(new_id):
    answer = new_id

    # 1번
    answer = answer.lower()

    # 2번
    temp = ''
    for i in range(len(answer)):
        if answer[i].isalpha() or answer[i].isdigit() or answer[i] == '-' or answer[i] == '_' or answer[i] == '.':
            temp += answer[i]
    answer = temp

    # 3번 --> 구현 오래 걸렸다.
    idx = 0    # idx는 계속 증가
    while answer[idx:].count('.') > 1:
        cnt = 0
        # 시작 idx가 '.'이고
        if answer[idx] == '.':
            # 다음으로 연속된 '.'을 찾는 과정
            for i in range(idx + 1, len(answer)):
                if answer[i] != '.':
                    break
                cnt += 1
            answer = answer[:idx] + '.' + answer[idx + cnt + 1:]
        idx += 1

    # 4번
    # 첫 번째 if에서 문자 삭제되어서 빈 문자열이 될 때 주의!
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:len(answer) - 1]

    # 5번
    if len(answer) == 0:
        answer = 'a'

    # 6번
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]

    # 7번
    if len(answer) <= 2:
        word = answer[-1]
        while len(answer) < 3:
            answer += word

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
