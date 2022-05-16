A = int(input())
B = int(input())

if ((A>0) & (B>0)):
    print('1')
elif((A<0) & (B>0)):
    print('2')
elif((A<0) & (B<0)):
    print('3')
else:
    print('4')
    
'''x, y = map(int, input().split())
if (0<x) & (0<y):
    print("1")
elif (x<0) & (0<y):
    print("2")
elif (x<0) & (y<0):
    print("3")
else:
    print("4")'''