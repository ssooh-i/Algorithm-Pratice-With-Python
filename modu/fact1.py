# 팩토리얼 버전 1, 일반 반복문
# def fact(n):
#     facto = 1;
#     for i in range(1,n+1):
#         facto = facto*i
#     return facto
#
# print(fact(10))

#팩토리얼 버전 2, 재귀함수
def fact2(n):
    if n <= 1:
        return 1
    return n * fact2(n - 1)

print(fact2(5))