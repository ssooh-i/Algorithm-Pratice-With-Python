# 피보나치 수열

def fibo(n):
    if n == 0: return 0
    if n == 1 or n == 2 : return 1
    return fibo(n - 1) + fibo(n - 2)

#책 정답 코드
def fibo2(n):
    if n <= 1:
        return n
    return fibo2(n - 1) + fibo2(n - 2)

# 재귀함수로 짜면 시간복잡도(O(2^n))가 가파르게 증가함
# 메모이제이션으로 구현
from functools import lru_cache

@lru_cache(maxsize=None) #@lru_cache 데코레이터의 추가로 한번 계산된 값을 바로 가져옴
def fibo3(n):
    if n == 0: return 0
    if n == 1 or n == 2 : return 1
    return fibo3(n - 1) + fibo3(n - 2)

print(fibo(5))
print(fibo(9))
print('---------')
print(fibo2(5))
print(fibo2(9))
print('---------')
print(fibo3(5))
print(fibo3(9))
n = 50
print('Fibonacci({}): {}'.format(n, fibo3(n)))
