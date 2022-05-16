a = input()
num = a
stack = 0
while 1:
        if len(num) == 1:
            num = "0" + num
            result = str(int(num[0]) + int(num[1]))
            num = num[-1] + result[-1]
            stack += 1
            if num == a:
                print(stack)
                break