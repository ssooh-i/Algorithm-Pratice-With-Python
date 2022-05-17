T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split(" ")))
    max_n = max(nums) #list 증 최대값 추출
    index = nums.index(max_n) #list 인덱스 번호 추출
    print(index)
