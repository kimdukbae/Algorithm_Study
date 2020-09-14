def solution(s):
    length = len(s)
    if length == 4 or length == 6:
        for i in range(length):
            if not s[i].isdigit():
                return False
        return True
    else:
        return False

# def solution(s):
#    return s.isdigit() and len(s) in [4,6]

# def solution(s):
#     return (len(s) == 4 or len(s) == 6) and s.isdigit() or False


res1 = solution('a234')
res2 = solution('1234')
print(res1)
print(res2)