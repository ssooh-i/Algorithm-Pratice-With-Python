A, B = map(int, input().split())
if ((A==1) & (B==3)) or ((A==3) & (B==1)):
    if A==1:
        print('A')
    else:
        print('B')
else:
    if A>B:
        print('A')
    else:
        print('B')
