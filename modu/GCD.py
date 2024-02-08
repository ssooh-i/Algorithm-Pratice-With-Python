# 최대공약수 GCD 구하기
def gcd(a, b):
    i = min(a, b)
    while True:
        if (a % i == 0) & (b % i == 0):
            # if a%i == 0 and b%i == 0: #책 정답
            return i
        else:
            i -= 1

print(gcd(1, 5))
print(gcd(4, 6))
print(gcd(3, 5))
print(gcd(60, 24))
print(gcd(81, 27))
print("----------------")
# 유클리드 알고리즘
# a와 b의 최대공약수는 b와 a를 b로 나눈 나머지의 최대공약수와 같다.
# gcd(a, b) => gcd(b, a%b)
def gcd2(a, b):
    if b == 0: #종료 조건
        return a
    return gcd2(b, a % b)


print(gcd2(1, 5))
print(gcd2(4, 6))
print(gcd2(3, 5))
print(gcd2(60, 24))
print(gcd2(81, 27))
