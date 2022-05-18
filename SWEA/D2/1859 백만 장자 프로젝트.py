# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     nums = list(map(int, input().split(" ")))
#     max_n = max(nums) #list 증 최대값 추출
#     index = nums.index(max_n) #list 인덱스 번호 추출
#     print(f"#{tc} ", end ="")
#     sum = 0
#     for i in range(0, N):
#         if nums[i] == max_n:
#             sum += 0
#             if nums[i] < max_n:
#                 sum += (max_n - nums[i])
#         else:
#                 sum += (max_n - nums[i])
#     print(sum)
    #     if nums[i] < max_n:
    #         #print(nums[i], max_n)
    #         sum += (max_n - nums[i])
    #         #print(sum)
    #         #sum += (max_n - nums[i])
    # # print(sum)
    # #         for j in range(i+1, N):
    # #             sum += (max_n-nums[j])
    # #             print("1", sum)
    #     elif nums[i] == max_n:
    #         sum += 0
    # print(sum)
    # # print("2",sum)

#역순으로 풀기
T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    max_n = nums[-1]
    #print(max_n)
    sum = 0
    for i in range(len(nums)-1,-1,-1): #역순으로 가지고 오기
        if max_n > nums[i]:
            sum += max_n-nums[i]
        else: # max_n =< nums[i] 경우
            max_n = nums[i]
    print(f"#{t} {sum}")

#for i ~
# 	for i +1 ~len(N)
# 	max
#
# i+1,
#
# _max 는 i+1번째부터 i부터 비교했을 때 최고가가 들어감
# i < _max면 그때 sum 값을 더해준다
