from collections import Counter
T = int(input())
for i in range(1, T+1):
    num = int(input())
    test_case = list(map(int, input().split(" ")))
    if len(test_case) == 1000:
        bin = Counter(test_case).most_common(1)
        bin1 = bin[0]
        bin2 = bin1[0]
        print("#"+str(i),bin2)
    else:
        print(-1)