'''
set함수를 이용해서 1부타 10000까지를 새로운 변수 natural로 설정하고
생성될 숫자를 generated 변수로 만들어준다

1부터 10000까지 반복문을 돌리고 2중 반복문으로 입력되는 i를 str로 바꿔서
n 값을 때어서 계산할 수 있게 만들어준다. 결과는 generated에 넣는다

전체 자연수에서 생성자가 모인 generated를 빼면 셀프넘버만 남는다.
새로운 for문을 만들어서 셀프넘버를 출력하게 한다
'''

numbers = set(range(1, 10000))
remove_set = set()  # 생성자가 있는 숫자 set
for num in numbers :
    for n in str(num):
        num += int(n)
    remove_set.add(num)  # add: 집합에 요소를 추가할 때

self_numbers = numbers - remove_set  # set의 '-' 연산자로 차집합을 구함
for self_num in sorted(self_numbers):  # sorted 함수로 정렬
    print(self_num)