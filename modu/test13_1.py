def self_palindrome(s):
    str = list(s.lower()) #소문자로 만들어놓기
    copy_cat = []
    str2 = []

    # 알파벳만 골라놓기
    for i in range(0, len(s), 1):
        if str[i].isalpha():
            str2.append(str[i])
    #골라놓은 알파벳 뒤집어서 만들어놓기
    for i in range(len(str2)-1, -1, -1):
        copy_cat.append(str2[i])

    for i in range(0, len(str2)):
        if str2[i] != copy_cat[i]:
            return False
    return True


print(self_palindrome("Wow"))
print(self_palindrome("Madam, I'm Adam."))
print(self_palindrome("Madam, I am Adam."))