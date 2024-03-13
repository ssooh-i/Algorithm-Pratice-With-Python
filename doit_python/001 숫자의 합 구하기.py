# 백준 11720번
# 입력 받기
n = input()
m = input()

# 입력된 숫자를 문자열로 변환
number_str = str(n)
number_str2 = str(m)

# 각 자리의 숫자를 분리하여 리스트로 만들기
digit_list = [int(digit) for digit in number_str]
digit_list2 = [int(digit2) for digit2 in number_str2]

# 각자 더해서 넣을 변수 만들기
total_n = 0
total_m = 0

# 각 리스트 자리수 더하기
for i in range(len(digit_list)):
    total_n += digit_list[i]
    #print("n의 합 : ", total_n)

for i in range(len(digit_list2)):
    total_m += digit_list2[i]
    #print("m의 합 : ", total_m)

# 결과 출력
if total_n > total_m:
    print(total_n)
elif total_m > total_n:
    print(total_m)
elif total_n == total_m:
    print(total_n)

# 책
a = int(input())
result = 0
sum_list = input()
for i in range(0, a):
    result += int(sum_list[i])

print(result)