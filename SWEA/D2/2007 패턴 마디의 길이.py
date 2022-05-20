#문제 케이스가 이상하여 백준 16229번 반복 패턴 문제로 대체함
n,m = map(int, input().split(" "))
s = list(input())
if len(s) > n:
    print('s input Error')
else:
    for j in range(0, m):
        for i in range(len(s), len(s)+m):
            s[i].append(s[j])
            print(s)