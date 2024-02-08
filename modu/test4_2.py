#나중에 다시풀기
#숫자 n개 중에서 최대값을 찾는 재귀호출을 만드시오
def max_num(V, n):
    if n == 1:
        return V[0]
    max_n_1 = max_num(V, n-1) #n-1개중 최대값을 구함
    if max_n_1 > V[n-1]:
        return max_n_1
    else:
        return V[n-1]

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(max_num(v, len(v))) #함수에 리스트의 자료개수를 인자로 추가해서 호출함