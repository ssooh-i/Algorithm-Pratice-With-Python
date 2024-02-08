def pair(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            print(a[i], " - ", a[j])

listA = ["Tom", "John", "Smith"]
pair(listA)
print()
listB = ["Tom", "John", "Smith", "John"]
pair(listB)