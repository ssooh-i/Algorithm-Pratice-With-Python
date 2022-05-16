'''def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("응용", 27, True)
say_myself("용용", 25, False)'''

'''a = 1
def vartest():
    global a
    a += 1
vartest()
print(a)'''

'''add = lambda a, b : a+b
result = add(3,4)
print(result)'''

'''result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))'''

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(7))
print(cal2.add(3))
print(cal2.sub(7))