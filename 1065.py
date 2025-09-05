n = int(input())
hansu = 0
for i in range(1, n + 1):
    if i < 100:
        hansu += 1
        continue

    is_ap = True
    arr = list(map(int, str(i)))
    diff = arr[0] - arr[1]

    for j in range(2, len(arr)):
        if arr[j - 1] - arr[j] != diff:
            is_ap = False
            break
    if is_ap:
        hansu += 1
print(hansu)
