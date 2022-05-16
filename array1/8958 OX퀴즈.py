# a = int(input())
#
# for i in range(a): #원하는 수만큼 반복
#     b = list(input())  # 입력받은 값 하나씩 잘라서 list형태로 변환하여 저장
#     score = 0
#     score_list = []
#     if b[i] == 'O':
#         score = score + 1
#     score_list.append(score)
# print(score)
#
# b = list(input())  # 입력받은 값 하나씩 잘라서 list형태로 변환하여 저장
# score = 0
# score_list = []
# for i in range (len(b)):
#     if b[i] == 'O':
#         score = score + 1
# score_list.append(score)
# print(score)
# print(score_list)

n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)