T = int(input())
A = 0
B = 0
for i in range(1, T+1):
    P,Q,R,S,W = list(map(int, input().split(" ")))
    A = P*W
    if W > R :
        B = ((W-R)*S)+Q
    else:
        B = Q
    if A > B:
        print("#"+str(i), B)
    elif A == B:
        print("#" + str(i), A)
    else:
        print("#" + str(i), A)