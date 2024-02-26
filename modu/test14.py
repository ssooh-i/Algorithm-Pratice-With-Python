def find_same_name(s):
    name_list = dict()

    for i in range(0, len(s), 1):
        if s[i] not in name_list:
            name_list[s[i]] = 1
        else:
            name_list[s[i]] += 1

    result = set()
    for n in name_list:
        if name_list[n] > 1:
            result.add(n)

    return result


name1 = ["Tom", "Jerry", "Mike", "Tom"]  # 대소문자 유의!, 파이썬은 대소문자 구분한다
print(find_same_name(name1))
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))
