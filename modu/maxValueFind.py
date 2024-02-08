def maxValueFind(a):
    maxValue = a[0]
    maxPosition =a[0]
    n = len(a)
    for i in range(1, n):
        if a[i] > maxValue:
            maxValue = a[i]
            maxPosition = i
    return maxPosition, maxValue

def minValueFind(a):
    minValue = a[0]
    minPosition =a[0]
    n = len(a)
    for i in range(1, n):
        if(a[i] < minValue):
            minValue = a[i]
            minPosition = i
    return minPosition, minValue

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(maxValueFind(v))
print(minValueFind(v))