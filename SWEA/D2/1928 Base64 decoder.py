# # base64 사전 만들기 예시
# base64_dict = {}
# char = 'A'
# index = 0
# while ord(char) != ord('Z')+1:
#     base64_dict[char] = index
#     char=chr(ord(char)+1)
#     index+=1
# print(base64_dict)
#
# # 10진법 숫자 -> 2진법 숫자 (6자리맞춰서)
# base64_maxLen = 6
# temp = format(10, "b") # int("001010", 2) # 2진법 ->10진법
# temp = '0' * (base64_maxLen - len(temp)) + temp
# print(temp)
#
# def base64_to_binary(base64_char):
#     """
#     base64형태의 문자가 입력되었을때,
#     이진법형태의 문자열로 바꿔서 return 해라
#     """
#     return ''
#
# def binary_to_ASCII(binary):
#     """
#     24bit 이진법형태의 문자열이 입력되었을때,
#     3개의 ASCII코드로 바꿔서 return 해라
#     """
#     return ''
#
# # 메인함수 예시
# print('#1')
# _input = input()
# for char in _input:
#     num = base64_dict[char]
#     b1 = base64_to_binary(char)
#     b2 = base64_to_binary(char)
#     b3 = base64_to_binary(char)
#     b4 = base64_to_binary(char)
#
#     binary = b1+b2+b3+b4
#
#     ascii = binary_to_ASCII(binary)
#     print(ascii, end='')
# print()
# ------------------
base64_dict = {}
char = "A"
index = 0
while ord(char) < ord('Z') + 1:
    base64_dict[char] = index
    char = chr(ord(char) + 1)
    index += 1

char = "a"
while ord(char) < ord('z') + 1:
    base64_dict[char] = index
    char = chr(ord(char) + 1)
    index += 1

char = "0"
while ord(char) < ord("9") + 1:
    base64_dict[char] = index
    char = chr(ord(char) + 1)
    index += 1

base64_dict['+'] = 62
base64_dict['/'] = 63

max_len = 6


def base64_to_binary(base64_char):
    """
    base64형태의 문자가 입력되었을때,
    이진법형태의 문자열로 바꿔서 return 해라
    """
    base64_num = base64_dict[base64_char]
    base64_num = format(base64_num, "b")
    result = "0" * (max_len - len(base64_num)) + base64_num

    return result


def binary_to_ASCII(binary):
    """
    24bit 이진법형태의 문자열이 입력되었을때,
    3개의 ASCII코드로 바꿔서 return 해라
    """
    result = ""
    for i in range(0, len(binary), 8):
        result += chr(int(binary[i:i+8], 2))
    return result


#print(base64_to_binary("b"))

T = int(input())
for tc in range(1, T+1):
    base64 = input()
    print(f"#{tc} ", end ="")

    for i in range(0, len(base64), 4):
        b1 = base64_to_binary(base64[i])
        b2 = base64_to_binary(base64[i+1])
        b3 = base64_to_binary(base64[i+2])
        b4 = base64_to_binary(base64[i+3])
        result = b1 + b2 + b3 + b4
        ascii_result = binary_to_ASCII(result)
        print(ascii_result,end="")
    print()