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

str_result = str(result)
num = []
len_str = len(str_result)

for j in range(0, len_str):
    count = list(str_result)
    if count[j] == 0:
        num[0] += 1
        j += 1

    elif count[j] == 1:
        num[1] += 1
        j += 1

    elif count[j] == 2:
        num[2] += 1
        j += 1

    elif count[j] == 3:
        num[3] += 1
        j += 1

    elif count[j] == 4:
        num[4] += 1
        j += 1

    elif count[j] == 5:
        num[5] += 1
        j += 1

    elif count[j] == 6:
        num[6] += 1
        j += 1

    elif count[j] == 7:
        num[7] += 1
        j += 1

    elif count[j] == 8:
        num[8] += 1
        j += 1

    else:
        num[9] += 1
        j += 1

        for i in range(0, 10):
            print(num[i])