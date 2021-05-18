from itertools import combinations


def solution(orders, course):
    answer = []
    for num in course:
        menu = {}
        for order in orders:
            order = list(order)
            order.sort()
            for comb in combinations(order, num):
                if comb in menu.keys():
                    menu[comb] += 1
                else:
                    menu[comb] = 1
        menu = sorted(menu.items(), key=lambda x: x[1])
        maximum = 0
        while menu:
            now_menu, cnt = menu.pop()
            if cnt <= 1:
                break
            else:
                if cnt >= maximum:
                    maximum = cnt
                    answer.append(''.join(now_menu))
                else:
                    break

    answer.sort()

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
