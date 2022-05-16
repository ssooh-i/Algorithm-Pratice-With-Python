n = int(input())
n_list = list(map(int, input().split(" ")))
idx = 0
med = 0
if 8 < n < 200:
    if (n % 2) == 1:
        n_list.sort() #오름차순으로 정렬
        idx = n//2 #값들의 중간값, // = 나누기 연산 후 소수점 버리고 정수만 추출
        med = n_list[idx]
        print(med)
    else:
        print(-2)

else:
    print(-1)