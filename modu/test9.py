# 쉽게 설명한 삽입 정렬 알고리즘

# 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
def find_ins_idx(r, v):
    # 이미 정렬된 리스트 r의 자료를 앞에서 부터 차례로 확인
    for i in range(0, len(r)):
        # v값보다 i번 위치의 값이 크면, v가 그 값 바로 앞에 놓여야 정렬이 유지된다.
        if r[i] > v:
            return i
    # 적절한 위치를 못 찾았을 때는, v가 r의 모든 자료보다 크다는 뜻으로 맨 뒤에 삽입
    return len(r)


def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)  # 기존 리스트에서 맨 앞의 값을 꺼낸다
        ins_idx = find_ins_idx(result, value)  # 꺼낸 값이 들어갈 적당한 위치 찾기
        result.insert(ins_idx, value)  # 찾은 위치에 값 삽입 (이후 값들은 한칸씩 밀림), append()는 맨 뒤에 추가임 insert(원하는 위치, 값)로 추가하기
        print(a, result)

    return result


d = [2, 4, 5, 1, 3]
print(ins_sort(d))
