testCase = int(input())
num_list = []
prime_number = [2,3,5,7,11]
for tc in range(testCase):
    num_list.append(int(input()))
for tc in range(testCase):
    prime_number_count = [0,0,0,0,0]
    num = num_list[tc]
    for i in range(5):
        while num % prime_number[i] == 0:
            prime_number_count[i] += 1
            num = num//prime_number[i]
    print("#" + str(tc+1),end=' ')
    for i in prime_number_count:
        print(i,end = ' ')
    print()