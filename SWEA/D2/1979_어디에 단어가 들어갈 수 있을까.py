"""
배열 탐색
"""

def col_check(y, x):
    _y = y
    while True:
        _y = _y+1
        if (_y >= len(words)):
            return _y-y

        visited_col[_y][x] = True
        if (words[_y][x] == 0):
            return _y-y

def row_check(y, x):
    _x = x
    while True:
        _x = _x+1
        if (_x >= len(words)):
            return _x-x

        visited_row[y][_x] = True
        if (words[y][_x] == 0):
            return _x-x

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    visited_col = [[False for _ in range(N)] for _ in range(N)]
    visited_row = [[False for _ in range(N)] for _ in range(N)]
    words = []
    for i in range(N):
        words.append(list(map(int, input().split())))

    answer = 0
    for y in range(N):
        for x in range(N):
            if (visited_col[y][x] is False) & (words[y][x] == 1):
                visited_col[y][x] = True
                if col_check(y,x) == K:
                    answer += 1

            if (visited_row[y][x] is False) & (words[y][x] == 1):
                visited_row[y][x] = True
                if row_check(y,x) == K:
                    answer += 1

    print(f"#{tc} {answer}")