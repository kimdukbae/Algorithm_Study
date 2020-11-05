# 내 풀이
# N, K = map(int, input().split())
# cnt = 0
#
# while True:
#     if N == 1:
#         print(cnt)
#         break
#
#     elif (N % K) == 0:
#         cnt += 1
#         N //= K
#
#     else:
#         cnt += 1
#         N -= 1



# 해법 1
# n, k = map(int, input().split())
# result = 0
#
# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#
#     n //= k
#     result += 1
#
# while n > 1:
#     n -= 1
#     result += 1
#
# print(result)
# while 문이 비교적 많은 것 같다...



# 해법 2
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)  # target(K로 나눠질 때) 까지 갈 때 1씩 빼줘야하는 동작
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)
print(result)