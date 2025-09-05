import math

def calc(index, check: list):
    if len(check) == n - 1:
        return arr[index][0] if arr[index][0] != 0 else math.inf
    result = math.inf
    for i in range(n):
        if i in check or arr[index][i] == 0:
            continue
        result = min(result, calc(i, check + [index]) + arr[index][i])
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

print(calc(0, []))