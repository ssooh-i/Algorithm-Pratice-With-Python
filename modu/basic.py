import math


def abs_sign(a):
    if (a >= 0):
        return a
    else:
        a = -a
        return a


def abs_square(a):
    b = a * a
    return math.sqrt(b)  # 수학모듈의 제곱근 함수


prt(abs_sign(5))
print(abs_square(5))
print()
print(abs_sign(-3))
print(abs_square(-3))
