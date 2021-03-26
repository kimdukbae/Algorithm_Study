def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


print(is_prime_number(4))
print(is_prime_number(11))
print(is_prime_number(257))
print()

# 위 알고리즘은 O(N)의 시간복잡도로 N이 커지면 시간복잡도도 꽤나 커지게 된다.
# 따라서 x까지 나눠떨어지는지 비교하지 말고 x의 제곱근까지만 확인해도 소수 판별 가능하다! --> 시간복잡도 줄일 수 있음
import math


def is_prime_number_faster(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False

    return True


print(is_prime_number(4))
print(is_prime_number(11))
print(is_prime_number(257))
