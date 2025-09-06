import sys


def merge_sort(arr: list):
    if len(arr) == 1:
        return arr

    a = merge_sort(arr[:len(arr) // 2])
    b = merge_sort(arr[len(arr) // 2:])

    pos = 0
    a_pos = 0
    b_pos = 0

    while len(a) > a_pos and len(b) > b_pos:
        if a[a_pos] < b[b_pos]:
            arr[pos] = a[a_pos]
            a_pos += 1
        else:
            arr[pos] = b[b_pos]
            b_pos += 1
        pos += 1

    for i in range(a_pos, len(a)):
        arr[pos] = a[i]
        pos += 1
    for i in range(b_pos, len(b)):
        arr[pos] = b[i]
        pos += 1

    return arr


n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(n)]

print(*merge_sort(arr))
