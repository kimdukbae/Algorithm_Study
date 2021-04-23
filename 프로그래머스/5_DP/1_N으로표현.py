def solution(N, number):
    ans = [[i, [int(str(N) * i)]] for i in range(1, 9)]
    for i in range(1, 8):
        for a in ans[i]:
            print(a)


    print(ans)


print(solution(5, 12))
print(solution(2, 11))
