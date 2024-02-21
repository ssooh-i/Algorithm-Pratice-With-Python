# 리스트에 찾는 값이 여러 개라면 그 위치 모두를 리스트로 알려주기
# 찾는 값이 없다면 [] 빈 리스트 출력
def search(a, x):
    n = len(a)
    result = []
    for i in range(0, n):
        if a[i] == x:
            result.append(i)
    return result

v1 = [1,1,2,3,4,5,6,7,8,9,10]
v2 = [1,2,2,3,4,5,6,7,8,2,10]

print(search(v1, 1))
print(search(v2, 2))