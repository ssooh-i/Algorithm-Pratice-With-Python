import sys

t = int(sys.stdin.readline())
for i in range(1, t+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A+B}") #f-formatting방식