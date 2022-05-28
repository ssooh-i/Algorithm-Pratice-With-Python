def solution(cacheSize, cities):
    cache = []
    time = 0
    for i in range(len(cities)):

        if cities[i].lower() in cache:
            time += 1
            del cache[cache.index(cities[i].lower())]
            cache.append(cities[i].lower())

        else:
            time += 5
            cache.append(cities[i].lower())

            if len(cache) > int(cacheSize):
                del cache[0]

    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])); # 50
print(solution(4, ["1", "2", "3", "4", "2"])); # 21
print(solution(30, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])); # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])); # 60
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])); # 60
print(solution(4, ["Jeju", "Pangyo", "NewYork", "newyork"])); # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])); # 25
print(solution(3, ["A", "B", "A"])); # 11
print(solution(10, ["1", "2", "3", "2"])); # 16
print(solution(0, ["A", "B", "A", "A", "A"])); # 25