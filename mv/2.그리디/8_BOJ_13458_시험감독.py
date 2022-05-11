import sys

input = sys.stdin.readline

N = int(input())  # 시험장 수
A = list(map(int, input().split()))  # 응시자 수
B, C = map(int, input().split())

answer = 0
for tester in A:
    if tester >= B:
        tester -= B
        answer += tester // C
        if tester % C != 0:
            answer += 1

print(answer + N)
