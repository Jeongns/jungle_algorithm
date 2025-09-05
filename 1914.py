def hanoi(cnt, a, b, c):
    if cnt == 1:
        print(a, c)
        return

    hanoi(cnt - 1, a, c, b)
    hanoi(1, a, b, c)
    hanoi(cnt - 1, b, a, c)
    return


n = int(input())

print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 2, 3)
