import sys

input = sys.stdin.readline
N = int(input())
test_sites = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0

for test_site in test_sites:
    # 부감독관 배치
    # (주의!) 총감독관 먼저 1명을 무조건 선정해야함. -> 문제에 해당조건이 있나?
    # 총감독관 1명만으로 시험인원 감독가능하면 아래 코드 실행 X -> 정답에서 +1 해줘서 총감독관만으로 시험인원 감독하게 함
    if test_site >= B:
        test_site -= B
        ans += test_site // C
        if test_site % C != 0:
            ans += 1

# 총감독관 배치 인원 수는 N이다. (총감독관은 오직 1명)
print(ans + N)
