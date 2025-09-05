def calc(n, x, y):
    if x == 0 and y == 0:
        return 0

    half = n // 2
    num = 0
    if x - half >= 0:
        x = x - half
        num += 1

    if y - half >= 0:
        y = y - half
        num += 2

    return calc(half, x, y) + (half ** 2) * num


n, r, c = map(int, input().split(" "))
print(calc(2 ** n, c, r))
