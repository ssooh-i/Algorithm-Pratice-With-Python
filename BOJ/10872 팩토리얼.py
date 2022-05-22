#그냥 풀기
# N = int(input())
# result = 1
# for i in range(N, 0, -1):
#     result += result*(N - i)
# print(result)

#재귀함수로 풀기
def factorial(N):
    if N == 0 & N == 1:
        return 1
    return N * factorial(N-1)
    ''' 
    ex) N = 5
    5*(4*(3*(2*(1))))
    '''

N = int(input())
print(factorial(N))