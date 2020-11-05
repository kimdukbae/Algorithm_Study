# 내가 구현한 답!
# N, M, K = map(int, input().split())
# arr = list(map(int, input().split()))
#
# great = max(arr)
# arr.remove(great)
#
# good = max(arr)
#
# cnt, ans = 0, 0
# for i in range(M):
#     if cnt == K:
#         ans += good
#         cnt = 0
#     else:
#         ans += great
#         cnt += 1
#
# print(ans)



# 해설집 -> 조금 비효율적인거 같다.
# 위의 내 코드가 더 효율적인듯

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
# 
# data.sort()
# first = data[n - 1]
# second = data[n - 2]
# 
# result = 0
# 
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
# 
#     if m == 0:
#         break
# 
#     result += second
#     m -= 1
# 
# print(result)



# 해설집2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k + (m % (k + 1))
# print(count)

result = 0

result += count * first
result += (m - count) * second

print(result)