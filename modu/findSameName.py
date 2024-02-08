def findSameName(a):
    n = len(a)
    overlap = set()
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                overlap.add(a[i])
    return overlap


nameList1 = ["Tom", "Jerry", "Mike", "Tom"]
nameList2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]

print(findSameName(nameList1))
print(findSameName(nameList2))
