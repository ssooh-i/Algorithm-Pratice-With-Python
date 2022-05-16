# n = int(input())
#
# for _ in range(n):
#     nums = list(map(int, input().split()))
#     avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
#     cnt = 0
#     for score in nums[1:]:
#         if score > avg:
#             cnt += 1  # 평균 이상인 학생 수
#     rate = cnt/nums[0] *100
#     print(f'{rate:.3f}%')
#
#
# a = int(input())
# count = 0
# for i in range(a):
#     list_score = list(map(int, input().split()))
#     score = (sum(list_score) - list_score[0])/list_score[0]
#     len_list = len(list_score)
#     for j in range(1, len_list):
#         if list_score[j] > score:
#             count += 1
#
#     rate = ((count / list_score[0]) * 100.0)
#     print(f"{rate:.3f}%")
#
#일섭이가 수정해준 답
# a = int(input())
# count = 0
# for i in range(a):
#     lists = list(map(int, input().split(" ")))
#     N = lists[0]
#     scores = lists[1:]
#     avg = sum(scores)/N
#     count=0
#     for j in range(0, N):
#         if scores[j] > avg:
#             count += 1
#
#     rate = ((count / N) * 100.0)
#     print(f"{rate:.3f}%")
