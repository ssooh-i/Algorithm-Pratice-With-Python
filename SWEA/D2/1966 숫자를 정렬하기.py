t = int(input())

for tc in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    nums.sort()
    print(f"#{tc} ", end="")
    for i in range(0, n):
        print(nums[i], end=" ")
    print()