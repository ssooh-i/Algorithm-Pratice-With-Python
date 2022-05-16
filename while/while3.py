import sys

n = input()
num = n
cnt = 0

while True:
        if len(num) == 1:
            num = "0" + num
        plus = str(int(num[0])+int(num[1]))
        num = num[-1] + plus[-1]
        cnt += 1

        if num == n:
            print(cnt)
            break