num = list(map(int, input().split()))
A = num[0]
B = num[1]
C = num[2]
#0과 1로 결과를 나누는 게 아니라 그냥 나머지를 고르는 거 였다
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)