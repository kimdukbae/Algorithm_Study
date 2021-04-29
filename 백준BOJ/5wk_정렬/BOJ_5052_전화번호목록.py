# if sum(map(lambda x: x.startswith(cur_num), phone[j])) > 0:
#     ans = "NO"
#     break
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    phone_num = [input().rstrip() for _ in range(N)]

    # 전화번호 목록 오름차순 정렬
    phone_num.sort()

    flag = False
    for i in range(N - 1):
        # 비교 번호가 바로 뒤에 있는 번호의 접두어인 경우인지 확인
        # --> 정렬되었기에 이 조건만으로도 일관성을 판단할 수 있다.
        if phone_num[i] == phone_num[i + 1][0:len(phone_num[i])]:
            flag = True
            break

    if flag:
        print('NO')
    else:
        print('YES')

