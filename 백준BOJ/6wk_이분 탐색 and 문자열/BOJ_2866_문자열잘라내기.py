# 왜 시간 초과 발생하는지 모르겠음...
import sys

input = sys.stdin.readline
r, c = map(int, input().split())
words = [list(input().rstrip()) for _ in range(r)]


def check():
    cnt = 0
    for _ in range(r - 1):
        del words[0]
        delete_words = list(map(str, zip(*words)))
        delete_words = set(delete_words)
        if len(delete_words) != c:
            return cnt
        cnt += 1

    return cnt


print(check())

# 추가 테스트 케이스
# 6 6
# qwerqy
# asdbgh
# zxcvbn
# aceeda
# abdbza
# cbedqc
