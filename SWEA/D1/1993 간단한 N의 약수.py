n = int(input())
nums = []
if(0<n<1001):
    for i in range(1, n+1):
        if (n%i == 0): #약수구하는 식
            nums.append(i)
for i in range(0, len(nums)):
    print(nums[i], end = ' ')