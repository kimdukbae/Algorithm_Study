# 에라토스테네스의 체는 여러 개의 수가 소수인지 아닌지 판별할 때 사용하는 알고리즘
# 1 ~ N 까지의 모든 소수를 구할 수 있는 알고리즘
import math

n = 1000
arr = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n) + 1)):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

# 2 ~ 1000 까지 모든 소수 출력
for i in range(2, n + 1):
    if arr[i]:
        print(i, end=' ')
