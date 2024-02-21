stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", " Mike", "Summer"]

def find_name(x):
    n = len(stu_no)
    for i in range(0, n):
        if stu_no[i] == x:
            return stu_name[i]
    return "?"

print(find_name(205))
