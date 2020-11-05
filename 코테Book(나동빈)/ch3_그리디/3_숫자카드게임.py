# 내 풀이
# N, M = map(int, input().split())
# cards = [0 for _ in range(N)]
#
# for i in range(N):
#     cards[i] = list(map(int, input().split()))
#
# ans = 0
# for card in cards:
#     low = min(card)
#     if low > ans:
#         ans = low
#
# print(ans)



# min() 함수를 이용한 해답
# n, m = map(int, input().split())
#
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
#
# print(result)
# 해답에서는 입력받자마자 비교하여 결과를 출력하도록 하였다.



# 2중 반복문으로 푼 해답
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001

    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)