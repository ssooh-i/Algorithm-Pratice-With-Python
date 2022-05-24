#오답
# for j in range(5):
#     arr = ['+' for i in range(5)]
#     arr[j] = "#"
#     print(*arr, end="")
#     print()

for i in range(5):
    for j in range(5):
        if i == j:
            print('#', end ="")
        else:
            print('+', end ="")
    print()