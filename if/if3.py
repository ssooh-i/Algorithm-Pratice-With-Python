year = int(input())
if ((year%4)==0):
    if ((year%100)!=0) or ((year%400)==0):
        print("1")
    else:
        print("0")
else:
    print("0")

'''year = int(input())
if((year%4 == 0) & (year%100 != 0))| (year%400 == 0):
    print('1')
else:
    print('0') #이게 위에 코드보다 짧고 시간도 4ms빠름'''