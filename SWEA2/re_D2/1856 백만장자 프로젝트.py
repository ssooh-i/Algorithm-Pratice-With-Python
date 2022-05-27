T = int(input())
for tc in range(1, T+1):
    n = int(input())
    N = list(map(int, input().split()))
    _sum = 0
    _max = max(N)
    for i in range(n-1, -1, -1):
        if _max > N[i]:
            _sum += _max - N[i]
    print(f"#{tc} {_sum}")

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