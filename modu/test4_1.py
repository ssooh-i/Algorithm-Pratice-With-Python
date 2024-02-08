#내가 푼 거
def sum(n):
    if n <= 1:
        return 1
    return n + sum(n-1)

print(sum(100))

#책 정답
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print()
print(sum(100))