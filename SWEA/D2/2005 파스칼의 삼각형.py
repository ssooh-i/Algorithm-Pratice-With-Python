T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = []
    for i in range(0, N):
        temp = []
        for j in range(i+1):
            if (j == 0) or (j == i):
                temp.append(1)
            else:
                temp.append(pascal[i-1][j] + pascal[i-1][j-1])
        pascal.append(temp)
    print(f"#{tc}")
    for i in pascal:
        print(*i) #*i : 각 리스트를 띄어쓰기만 해서 표기하는 방법

'''
조합 nCr = n!/r!(n-r)!
파스칼의 삼각형
nC0, nCn = 1
n-1 C r-1 + n-1 C r = nCr 성립
(2C1 + 2C2 = 3C2)
'''