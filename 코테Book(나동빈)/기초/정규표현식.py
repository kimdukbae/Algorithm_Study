# <Python 정규표현식>
# 정규표현식이란?
# 정규표현식을 줄여서 간단히 정규식이라고도 한다.
# 복잡한 문자열을 처리할 때 사용하는 기법!
# Python 뿐만 아니라 문자열을 처리하는 모든 곳에서 사용됨.
# 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어이다.
# 복잡한 문자열의 검색과 치환을 위해 사용됨. Python 뿐만 아니라 문자열을 처리하는 모든 곳에서 사용됨.
# 정규표현식을 잘 다루면 Python 외에 또 하나의 강력한 무기를 얻게 되는 것!

# 정규표현식이 왜 필요할까?
# 다음과 같은 문제가 주어졌다고 가정해 보자.
# 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 '*'로 변경해보자.
# 먼저 정규표현식을 모르는 상태라면, 아래와 같은 코드를 작성해야한다.

data = """
park 950101-1234567
lee  890212-3456789
"""

result = []
# 1. data를 Enter 단위로 나누기 위한 코드
for line in data.split("\n"):
    word_result = []
    # 2. (ex) park 950101-1234567 을 park과 950101-1234567로 나누기 위한 코드
    for word in line.split(" "):
        # 3. 주민등록번호인지 확인하는 조건
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# 구현하기 쉽다고 생각할 수 있다. 하지만, 정규표현식을 사용하면 훨씬 간단하게 구현할 수 있다.
# 정규표현식을 사용하면 더 쉽고 빠르게 구현할 수 있는데, 쓰지 않을 이유가 없다고 생각한다.
# 이후 포스팅에서 더 자세히 설명할 예정이기 때문에 정규표현식의 예제코드를 너무 이해하려 하지 말자. 정규표현식의 맛보기라 생각하자.

import re

data = """
park 950101-1234567
lee  890212-3456789
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

# 위와 같이 코드가 간결해지며 쉽고 빠르게 구현할 수 있다.
# 만약 처리하려는 문자열이 복잡해지고 길어지면 정규표현식의 사용이 더욱 필요하게 된다.

# -------------------------------------------------
# 2부

# 정규표현식 정리
# 정규표현식에서 사용하는 메타 문자(meta characters)에는 아래와 같은 것이 있다.
# 메타 문자 --> 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자를 의미함.
# . ^ $ * + ? { } [ ] \ | ( )
# 정규 표현식에 위 메타 문자를 사용하면 특별한 의미를 갖게됨!

# ---

# 1. 문자 클래스 []
# '[] 사이의 문자들과 매치'라는 의미를 가짐
# ※ 문자 클래스를 만드는 메타 문자 [] 사이에는 어떤 문자도 들어갈 수 있다.

# 다음 정규식을 보자
# [abc] --> a,b,c 중 한 개의 문자와 매치를 의미함
# a # 정규식과 일치하는 문자인 'a'가 있으므로 매치 O
# before # 정규식과 일치하는 문자인 'b'가 있으므로 매치 O
# ddr # a,b,c 중 하나라도 포함하고 있지 않으므로 매치 X
# 표 --> https://devkingdom.tistory.com/131


# ---
# 2. Dot(.)
# Dot(.) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미함.
# ※ 정규식을 작성할 때 re.DOTALL 옵션을 주면 \n 문자와도 매치된다.

# 다음 정규식을 보자
# a.b --> "a + 모든문자 + b" , 즉 a와 b라는 문자 사이에 어떤 문자가 들어가도 모두 매치된다는 의미.
# aab # a와 b사이에 a가 있으므로 정규식과 매치 O
# a0b # a와 b사이에 0이 있으므로 정규식과 매치 O
# abc # a와 b사이에 어떤 문자가 없으므로 매치 X

# 혼동 주의!
# 다음 정규식2를 보자
# a[.]b --> "a + Dot(.)문자 + b"
# 위 정규식과 달리 []내에 Dot(.) 메타 문자가 사용되면 "모든 문자"라는 의미가 아니다. 문자 . 그대로를 의미한다!! (혼동 주의!)
# a.b # a와 b사이에 .있으므로 정규식과 매치 O
# a0b, aab, abc # a와 b사이에 .이 없으므로 정규식과 매치 X


# ---
# 3. 반복 (*)

# 다음 정규식을 보자
# ca*t --> *은 *바로 앞에 있는 문자 a가 0부터 무한대로 반복될 수 있다는 의미이다.
# ※ 여기서 무한대라고 했는데 사실상 메모리 제한으로 2억개 정도까지라고 한다.
# ct # a가 0번 반복되어 매치 O
# cat # a가 1번 반복되어 매치 O
# caaat # a가 3번 반복되어 매치 O


# ---
# 4. 반복 (+)
# +는 최소 1번 이상 반복될 때 사용한다. (*는 최소 반복 횟수가 0부터라면, +는 반복 횟수가 1부터 이다.)
# 다음 정규식을 보자.
# ca+t --> "c + a(1번 이상 반복) + t"
# ct # a가 0번 반복되어 매치 X (1번 이상 반복되어야함)
# cat # a가 1번 반복되어 매치 O
# caaat # a가 3번 반복되어 매치 O


# 5. 반복 ({m, n}, ?)
# 반복을 고정 및 제한할 수도 있다.
# {m, n} 정규식을 사용하면 반복 횟수가 m부터 n까지 매치할 수 있다. 또한, m 또는 n을 생략할 수도 있다.또한
# # {3,}이면 반복 횟수가 3이상인 경우이고
# # {,3}이면 반복 횟수가 3이하를 의미한다.
# # m은 0과 동일하며, 생략된 n은 무한대(2억 개 미만)의 의미를 갖는다.
# ※ {1,}은 +와 동일하고, {0,}은 *와 동일하다.

# 다음 정규식을 보자.
# ca{2,5}t --> "c + a(2~5회 반복) + t"
# cat # a가 1번만 반복되어 매치 X
# caat # a가 2번 반복되어 매치 O
# caaaaat # a가 5번 반복되어 매치 O

# 다음 정규식을 보자.
# ab?c --> "a+b(있어도 되고 없어도 된다) + c"
# abc --> b가 1개 있어서 매치 O
# ac --> b가 없어서 매치 O


# -------------------
# Python에서 정규표현식 사용하기
# import re
# p = re.compile('ab*')
# 위와 같이 Python에서는 정규표현식 지원 re(regular expression) 모듈을 제공한다.
# re.compile을 사용하여 정규표현식 (ab*)을 컴파일한다. re.compile의 결과로 돌려주는 객체 p(컴파일된 패턴 객체)를 사용하여 그 이후의 작업을 처리한다.
# ※ 패턴이란 정규식을 컴파일한 결과이다.

# 정규표현식을 이용한 문자열 검색
# 컴파일된 패턴 객체를 사용하여 문자열 검색을 수행해보자. 컴파일된 패턴 객체는 4가지 메소드를 제공한다.
# Method        목적
# match() --> 문자열의 처음부터 정규식과 매치되는지 조사한다.
# search() --> 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
# findall() --> 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
# finditer() --> 정규식과 매치되는 모든 문자열(substring)을 반복 가능한(iterable) 객체로 돌려준다.

# match, search는 정규식과 매치될 때는 match 객체를 돌려주고, 매치되지 않을 때는 None을 돌려준다.


# 1. match
# 문자열의 처음부터 정규식과 매치되는지 조사한다.
import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)
# >>> <re.Match object; span=(0, 6), match='python'>
# 'python' 문자열은 [a-z]+ 정규식에 부합되므로 match 객체를 돌려준다.

m = p.match("3 python")
print(m)
# >>> None
# '3 python'은 '3' 때문에 [a-z]+ 정규식에 부합되지 않으므로 None을 돌려준다.


# match 메소드는 결과를 match 객체 또는 None으로 return 하기 때문에 아래와 같이 구현한다.
import re
p = re.compile('[a-z]+')
m = p.match('string goes here')
if m:
    print('Match found: ', m.group())
else:
    print('No match')



# 2. search
p = re.compile('[a-z]+')
m = p.search("python")
print(m)
# >>> <re.Match object; span=(0, 6), match='python'>
# search 메소드를 수행하면 match와 동일한 결과가 나온다.

# 그러나
p = re.compile('[a-z]+')
m = p.search("3 python")
print(m)
# >>> <re.Match object; span=(2, 8), match='python'>
# match와 다르게 search는 문자열의 처음부터가 아닌 전체를 검색하기 때문에 '3'이후 'python'의 문자열과 매치된다.
# search와 match의 차이라고 볼 수 있다.


# 3. findall
p = re.compile('[a-z]+')
result = p.findall("life is too long")
print(result)
# >>> ['life', 'is', 'too', 'long']
# life, is, too, short 단어를 각각 정규식과 매치해서 리스트로 돌려준다.


# 4. finditer
p = re.compile('[a-z]+')
result = p.finditer("life is too long")
print(result)
# >>> <callable_iterator object at 0x019D7A50>

for r in result: print(r)
# >>> <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 16), match='long'>

# finditer는 findall과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 돌려준다. 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.


# 그렇다면 findall은 리스트형태로 돌려주나 나머지 메소드들은 match 객체를 돌려준다. match 객체를 어떻게 사용할 수 있을지에 대해 알아보겠다.
# match 객체의 메소드
# match 객체의 메소드이다.
# 어떤 문자열이 매치되었는지, 매치된 문자열의 인덱스를 알 수 있다.
# Method        목적
# group() --> 매치된 문자열을 돌려준다.
# start() --> 매치된 문자열의 시작 위치를 돌려준다.
# end() --> 매치된 문자열의 끝 위치를 돌려준다.
# span() --> 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.

p = re.compile('[a-z]+')
m = p.match('python')
print(m.group())
print(m.start())
print(m.end())
print(m.span())
# >>> python
# >>> 0
# >>> 6
# >>> (0, 6)

