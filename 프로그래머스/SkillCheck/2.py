def solution(x):
    answer = True
    s = str(x)

    if x < 1 or x > 10000:
        answer = False
        return answer

    else:
        divide = 0
        for i in range(len(s)):
            divide += int(s[i])

        if x % divide != 0:
            answer = False
            return answer

    return answer


res1 = solution(10)
res2 = solution(12)
res3 = solution(11)
res4 = solution(13)

print(res1)
print(res2)
print(res3)
print(res4)