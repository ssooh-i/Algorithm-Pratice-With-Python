def find_student_name(s, n):
    if n in s:
        return s.get(n)
    else:
        return "?"

student = {39: "Justin", 14:"John", 67:"Mike", 105:"Summer"}
print(find_student_name(student, 14))
