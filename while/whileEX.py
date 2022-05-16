'''treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print(f"나무를 {treeHit}번 찍었습니다")
    if treeHit == 10:
        print("나무가 넘어갑니다")'''

'''coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1
    elif money > 300:
        print("거스름 돈은 %d를 주고 커피를 줍니다" %(money-300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지않습니다.")
        print("남은 커피의 양은 %d가 됩니다." %coffee)
    if coffee == 0:
        print("커피가 모두 소진되어 판매를 중지합니다.")
        break'''

#점프투파이썬 연습문제 1
'''a = "Life is too short, you need python"
if "wife" in a: print("wife") #X
elif "python" in a and "you" not in a: print("python") #X
elif "shirt" not in a: print("shirt") #shirt출력
elif "need" in a: print("need") #need출력이겠지만 가장 먼저 참이되는 세번쨰 조건만 출력됨
else: print("none") #X'''

#점프투파이썬 연습문제 2
'''tmp = 0
a = 0
while a < 1001:
    a += 1
    if a%3==0:
        tmp = tmp + a
print(tmp) #166833출력/ 정답
'''

#점프투파이썬 연습문제 3
'''i = 1
while i < 6:
    print(i*'*')
    i += 1 #정답'''

#점프투파이썬 연습문제 4
'''for i in range(1, 101):
    print(i) #정답'''

#점프투파이썬 연습문제 5
'''A = [70, 60, 55, 75, 95, 90, 80, 85 ,80, 100]
i = 0
add = 0
for i in range(len(A)):
    add += A[i]
print(add/10) # 79.0 출력 '''

#점프투파이썬 연습문제 6
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2 == 1] #리스트 내포방식 다시보기
print(result) 