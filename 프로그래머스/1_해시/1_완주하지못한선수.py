# 1. completion 안에 participant 에 해당하는 사람이 존재하는지 체크
# 2. 있으면 participant 에서 완주한 사람 지우기
# 3. participant 출력

# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[i + 1]



# import collections
# # collections 모듈은 파이썬의 범용 내장 컨테이너 dict, list, set, tuple
# # 등에 대한 대안을 제공하는 특수 컨테이너 데이터형을 구현
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
# # Counter()는 dict 와 같이 hash형 자료들의 값으 개수를 셀 때 사용
# # dict 처럼 {'자료이름':'개수'} 형식으로 만들어짐
# # Counter 객체들끼리 뺄셈 가능



# https://ychae-leah.tistory.com/23
# hash()를 활용한 뺄셈 연산
# 정답이 1개일 때만 유효
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for par in participant:
#         dic[hash(par)] = par
#         temp += int(hash(par))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]
#
#     return answer





p = ['leo', 'kiki', 'eden', 'leo']
c = ['eden', 'kiki', 'leo']
result = solution(p, c)
print(result)


