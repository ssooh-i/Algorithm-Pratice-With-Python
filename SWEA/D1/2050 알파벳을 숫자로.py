a = input()
a1 = list(a)
a2 = []
for i in range(0, len(a1)):
     a2.append(ord(a1[i]) - 64)
for i in range(0, len(a2)):
    print(a2[i], end=" ")

"""
#1 문자열을 list화 해서 문자 하나씩으로 쪼개는 방법
a1 = list(a) 로 쓰면 바로 list에 하나씩 들어가게됨 
(띄어쓰기로 구분된 여러개의 문자 입력 값을 list에 넣고 싶은 경우)
a1 = list(input().split())
(띄어쓰기로 구분된 여러개의 숫자 입력 값을 list에 넣고 싶은 경우 map을 이용)
a1 = list(map(int, input().split()))

#2 문자를 아스키코드로 변환하는 방법 (+ 그 외(아스키->문자)의 방법)
문자 -> 아스키 코드 변환: ord()
아스키 코드 -> 문자 변환: chr()
"""