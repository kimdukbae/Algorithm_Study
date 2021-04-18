import sys

N = int(sys.stdin.readline())

# 시간복잡도 조금이라도 줄이기 위해 666부터 시작
cnt, movie = 0, 666
while 1:
    if '666' in str(movie):
        cnt += 1
        if cnt == N:
            print(movie)
            break
    movie += 1
