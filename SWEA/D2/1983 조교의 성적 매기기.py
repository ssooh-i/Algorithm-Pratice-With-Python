T = int(input())
grade = ['A+', 'A0', 'A-','B+', 'B0', 'B-','C+', 'C0', 'C-','D0']
for tc in range(1, T+1):
    N, K = map(int, input().split())
    g = N/10
    arr = []
    result = []
    result2 = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    #N명의 학생 총 성적 매기기
    for i in range(len(arr)):
        temp = 0
        for j in range(3):
            print(arr[i][j])
            if j == 0:
                temp += arr[i][j] * 0.35
            elif j == 1:
                temp += arr[i][j] * 0.45
            else:
                temp += arr[i][j] * 0.2

        result.insert(i, temp)
        result2.insert(i, temp)
    result.sort(reverse=True)
    print(result)

    #학점주기
    re = []
    for i in range(len(result)):
        for _ in range(g):
            re.append(grade[i])

    #K 학생 학점 찾기
    for i in range(len(result)):
        if result2[K-1] == result[i]:
            print(grade[i])

    print(result)