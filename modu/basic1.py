# import math

# def abs_sign(a):
#     if (a >= 0):
#         return a
#     else:
#         a = -a
#         return a
# def abs_square(a):
#     b = a * a
#     return math.sqrt(b)  # 수학모듈의 제곱근 함수
# print(abs_sign(5))
# print(abs_square(5))

# def sum(a):
#     b = 0
#     for i in range(1, a+1): #1부터 a까지
#         b += i
#     return b
#
# def sum_n(a):
#     return a*(a+1)//2
#
# print(sum(100))
# print(sum_n(100))def sum(a):
# #     b = 0
# #     for i in range(1, a+1): #1부터 a까지
# #         b += i
# #     return b
# #
# # def sum_n(a):
# #     return a*(a+1)//2
# #
# # print(sum(100))
# # print(sum_n(100))

def sum_square(N):
    sum = 0
    for i in range(1, N + 1):
        sum = sum + (i * i)
    return sum


def square_sum(N):
    return N * (N + 1) * ((2 * N) + 1) // 6


print(sum_square(10))
print(square_sum(10))
