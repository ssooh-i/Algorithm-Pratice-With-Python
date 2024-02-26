# 회문 찾기 (큐와 스택)
from copy import copy

def palindrome(s):
    str = s.lower()
    qu = []
    st = []

    for x in str:
        # 해당문자가 알파벳이면(공백, 특수 문자, 숫자 X)
        if x.isalpha():
            qu.append(x)
            st.append(x)
    # 큐와 스택에 들어있는 문자를 꺼내면서 비교
    while qu: # 큐에 문자가 남아있는 동안 반복
        if qu.pop(0) != st.pop():
            return False
    return True


# 특수문자를 고려 안해서 탈락!
def self_palindrome(s):
    str = list(s.lower())
    copy_cat = copy(str)
    copy_cat.reverse()

    for i in range(0, len(s)):
        if str[i] != copy_cat[i]:
            return False
        return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))
print()
print(self_palindrome("Wow"))
print(self_palindrome("Madam, I'm Adam."))
print(self_palindrome("Madam, I am Adam."))