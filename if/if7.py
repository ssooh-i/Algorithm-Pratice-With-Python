a,b,c = map(int, input().split())
money = 0
if (a == b)&(a == c):
    money = 10000+(a*1000)
    print(money)
elif (a == b) | (a == c):
    money = 1000 + (a * 100)
    print(money)
elif (b == c) | (a == b):
    money = 1000 + (b * 100)
    print(money)
else:
    if ((a > b) & (a > c)): #a가 가장 클 때
        money = 100 * a
        print(money)
    elif ((a < b) & (b > c)): #b가 가장 클 때
        money = 100 * b
        print(money)
    else:
        money = 100 * c
        print(money)