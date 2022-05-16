n = input() #숫자로 친 문자열 받기
n_list = list(map(int, str(n))) #문자열인 n을 int형으로 변환해서 list안에 넣어줌
re = 0 # 결과 저장
for i in range(0, len(n_list)): #리스크 길이만큼 반복
    re = n_list[i] + re #리스트 안에 있는 것 끼리 더하기
print(re)
#-----------------------
n = list(map(int, input())) #숫자로 받아서 list안에 두기
re = 0 #결과값 넣을 자리
for i in range(0, len(n)):
    re = re + n[i]
print(re)