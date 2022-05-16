num = list(map(int, input().split()))
a = num[0]
b = num[1]
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")