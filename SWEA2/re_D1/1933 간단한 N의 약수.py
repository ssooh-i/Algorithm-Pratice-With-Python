N = int(input())
arr = []
for i in range(1, N+1):
    if (N%i) == 0:
        arr.append(i)
    arr.sort()
print(*arr)