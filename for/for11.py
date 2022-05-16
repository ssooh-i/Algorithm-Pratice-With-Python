'''a, b = map(int(input().split()))
test = []
for i in range(1, a+1):
    test = int(input())
    for j in range(len(test)):
        if test[j] > b:
            print(test[j])'''

import sys

N,X = map(int, sys.stdin.readline().split())
if(N,X >=1 and N,X <= 10000) :
    A = list(map(int, input().split()[:N]))
    for i in A :
        if i < X :
            print(i, end=' ')
