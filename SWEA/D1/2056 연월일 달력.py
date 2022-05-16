t= int(input())
month1 = ["1", "3", "5", "7", "8", "10", "12"]
for i in range(1, t+1):
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    if 0 < int(month) < 13:
        if month in month1: #month1 안에 있는 값/ list 속에 있는지 확인은 in 사용
            if 0< int(day) < 32:
                print("#"+str(i), year+"/"+month+"/"+day)
            else:
                print("#" + str(i), -1) #그냥 i를 쓰게되면 int형이라 오류남 str()로 감싸주기
        elif int(month) == 2: #2월일때
            if int(day) < 29:
                print("#"+str(i), year + "/" + month + "/" + day)
            else:
                print("#" + str(i), -1)
        else:
            if 0< int(day) < 31:
                print("#"+str(i), year+"/"+month+"/"+day)
            else:
                print("#" + str(i), -1)
    else:
        print("#"+str(i), -1)