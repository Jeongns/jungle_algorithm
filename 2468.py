import sys
sys.setrecursionlimit(1000000)

dfs = [[False] * 100 for i in range(100)]
x_move = [0, 1, 0, -1]
y_move = [1, 0, -1, 0]


def calc(x, y, h):
    if dfs[y][x] or area[y][x] <= h:
        return 0
    dfs[y][x] = True
    for i in range(4):
        if 0 <= x + x_move[i] < n and 0 <= y + y_move[i] < n:
            calc(x + x_move[i], y + y_move[i], h)
    return 1


n = int(input())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

result = 1
sum = 0
for h in range(1, 101):
    for x in range(n):
        for y in range(n):
            sum += calc(x, y, h)
    result = max(result, sum)
    sum = 0
    dfs = [[False] * 100 for i in range(100)]

print(result)
