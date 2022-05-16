hour,minute = map(int, input().split())
cook = int(input())

hour += cook//60
minute += cook%60

if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24

print(hour,minute)
'''
h=(hour +((minute+cook)//60))%24 #나누기 연산 후 소수점이하 버리고 정수부분만 추출

m=(minute +cook)%60
print(h,m)'''