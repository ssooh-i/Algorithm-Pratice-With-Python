#백준 2577번 숫자의 개수

count = None
result = None
while True:
    A = input()
    B = input()
    C = input()

    if (int(A)<100 | 1000<int(A)):
        pass
    else:
        while True:
            if(int(B)<100 | 1000<int(B)):
                pass
            else:
                while True:
                    if (int(C) < 100 | 1000 < int(C)):
                        pass
                    else:
                        result = int(A)*int(B)*int(C)
                        print(result) #A*B*C곱한 값
                        break
            break
    break

#count  = list(map(int, result))
#print(count)
num0, num1, num2,num3, num4,num5,num6,num7,num8,num8, num9 = 0
for j in range(0, len(result)):
    count = list(result)
    if count[j] == 0:
        num0 += 1
    elif count[j] == 1:
        num1 += 1
    elif count[j] == 2:
        num2 += 1
    elif count[j] == 3:
        num3 += 1
    elif count[j] == 4:
        num4 += 1
    elif count[j] == 5:
        num5 += 1
    elif count[j] == 6:
        num6 += 1
    elif count[j] == 7:
        num7 += 1
    elif count[j] == 8:
        num8 += 1
    else:
        num9 += 1

    for i in range(9):
        print(num[i])