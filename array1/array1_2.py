#백준 2562번 최댓값

'''x = [0,0,0,0,0,0,0,0,0] #리스트 X에 0으로 초기화한 list를 만듦
for i in range(0, 9): #0부터 8까지 9번 반복
    x[i]  = int(input()) #i번째에 계속 int형 값을 받음

print(max(x)) #max함수를 써서 list x의 최대값을 가져옴
print(x.index(max(x))) #index함수를 사용하여 배열에서 원하는 값의 위치를 찾음'''

num_list = [] #빈 배열만듦
for i in range(9): #9번 반복
    num_list.append(int(input())) #append로 배열에 추가

print(max(num_list)) #max로 최대값 나오게 하기
print(num_list.index(max(num_list)) + 1) #인덱스는 0부터 시작하기 때문에 +1 해준다