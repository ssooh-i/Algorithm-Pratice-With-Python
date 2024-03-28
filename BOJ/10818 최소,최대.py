import sys
input = sys.stdin.readline
N = int(input())
listA = list(map(int,input().split()))
print(min(listA), max(listA))