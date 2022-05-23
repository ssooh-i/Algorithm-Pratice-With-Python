def Fibonacci(N):
    if N == 0:
        return 0
    elif (N == 1) | (N == 2):
        return 1
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)

N = int(input())
print(Fibonacci(N))