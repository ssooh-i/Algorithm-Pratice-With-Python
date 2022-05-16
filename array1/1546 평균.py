a = int(input())
b = list(map(int, input().split())) #입력받은 값 하나씩 잘라서 list형태로 변환하여 저장
max_b = max(b) #max()써서 그중에 최고값 찾음

for i in range(a): #원하는 수만큼 반복
    b[i] = b[i]/max_b*100 #점수/M*100이라는 주어진 식으로 계산
print("%.2f" %(sum(b)/a)) #-10^2인 .2f하고 평균값 = 계산한 b값 전체, a로 나누기