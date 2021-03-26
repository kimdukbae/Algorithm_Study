a = 157.93
print(a)

a = -1837.2
print(a)

a = 5.
print(a)

a = -.7
print(a)

# Java에서 Integer.MAX_VALUE 와 비슷
a = 1e9
print(a)

a = 75.25e1
print(a)

a = 3954e-3
print(a)

# 2진수에서 0.9를 정확히 표현할 수 없음
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

# round(실수형 데이터, 반올림하고자 하는 위치 - 1)
# (ex) round(3.14, 1) --> 소수점 둘째 자리에서 반올림해서 3.1
print(round(a, 2))

# -------------------------------------------------------------------------
# 리스트(배열, 테이블) --> C++의 STL vector와 유사
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 빈 리스트 생성
a = list()
print(a)

a = []
print(a)

# 리스트 컴프리헨션
arr = [i for i in range(20) if i % 2 == 1]
print(arr)

arr2 = [i * i for i in range(1, 10)]
print(arr2)

row = 3
col = 4
board = [[0] * col for _ in range(row)]
print(board)

# .append() --> 리스트 삽입  O(1)
# .sort() --> 원본 리스트 오름차순 정렬  O(NlogN)
# .sort(reverse = True) --> 원본 리스트 내림차순 정렬  O(N)
# .insert(삽입할 위치 인덱스, 삽입할 값) --> 특정한 인덱스 위치에 원소를 삽입  O(N)
# .reverse() --> 리스트 원소의 순서 모두 뒤집음  O(N)
# .count(특정 값) --> 리스트의 특정 값을 가지는 데이터의 개수를 세줌  O(N)
# .remove(특정 값) --> 특정 값 원소 삭제, 특정 값 원소가 여러 개면 하나만 제거  O(N)


# 코테에서 remove() 남발하면 시간초과 뜸 그래서 아래의 방법 사용
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]
result = [i for i in a if i not in remove_set]
print(result)


# -------------------------------------------------------------------------
# 람다식
def add(x, y):
    return x + y


print(add(3, 7))
print((lambda x, y: x + y)(3, 7))

answer = 8
print("정답은", answer, "이다.")
print("정답은 " + str(answer) + "이다.")
print(f"정답은 {answer}이다.")

# -------------------------------------------------------------------------
# 라이브러리
# itertools : 순열과 조합 라이브러리 제공
# heapq : 힙(Heap) 기능을 제공하는 라이브러리, 우선순위 큐 기능을 구현하기 위해 사용
# bisect : 이진 탐색 기능을 제공하는 라이브러리
# collections : deque, Counter 등의 자료구조를 포함하고 있는 라이브러리
# math : 팩토리얼, 제곱근, GCD(최대공약수), 삼각함수 등 수학적 기능을 제공하는 라이브러리


# <내장 함수>
result = sum([1, 2, 3, 4, 5])
print(result)

result = min([7, 3, 5, 2])
print(result)

result = max([7, 3, 5, 2])
print(result)

# 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산함
result = eval("(3 + 5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

# 리스트 원소의 튜플의 2번째 원소를 기준으로 내림차순 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50), ('김덕배', 15)], key=lambda x: x[1], reverse=True)
print(result)

data = [9, 1, 8, 5, 4]
data.sort()
print(data)

# ★ sort() vs sorted() 의 차이
# data.sort() --> 원본 리스트 자체의 순서를 변경한다.
# sorted(data) --> 원본 리스트에는 영향 X / 정렬된 새로운 리스트를 반환함 / 리스트, 튜플, 딕셔너리, 문자열 등 모든 iterable에 동작한다.



# <itertools>
# 순열
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# 조합
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

# 중복순열
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

# 중복조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)



# <heapq>
# PriorityQueue 라이브러리를 사용할 수 있지만, 코테 환경에서는 보통 heapq가 더 빠르게 동작하므로 heapq 사용 권장!!
# Python 에서 힙은 최소 힙으로 구성되어 있음 --> 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN) 에 오름차순 정렬이 완료됨.
import heapq


def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# 또한, Python에서는 최대 힙을 제공 X --> heapq 라이브러리로 최대 힙을 구현할 때는 원소의 부호를 임시로 변경하는 방식 사용
def heapsort_reverse(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


result = heapsort_reverse([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)



# <bisect>
# bisect_left(a, x) --> 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메소드
# bisect_right(a, x) --> 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메소드
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# 위 함수는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구할 때 효과 최고!
def count_by_range(b, left_value, right_value):
    right_index = bisect_right(b, right_value)
    left_index = bisect_left(b, left_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))



# <collections>
# Python에서 Queue 라이브러리가 있는데 우리가 생각하는 일반적인 큐 자료구조가 아니다!
# 따라서 collections의 deque를 이용해 꼭 큐를 구현해야함!!
# deque 에서 리스트 처럼 인덱싱, 슬라이싱 등 기능 사용 불가! 하지만, 연속적으로 나열된 데이터의 시작 혹은 끝 부분에 데이터를 삽입, 삭제할 때는 매우 효과적
from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

# collections의 Counter는 등장 횟수를 세는 기능을 제공. 구체적으로 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지 알려줌.
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # 3
print(counter['green']) # 1
print(dict(counter))



# <math>
import math
print(math.factorial(5))    # 팩토리얼

print(math.sqrt(7))     # 제곱근

print(math.gcd(21, 14))     # 최대공약수

print(math.pi)  # 파이
print(math.e)   # 자연상수 e

