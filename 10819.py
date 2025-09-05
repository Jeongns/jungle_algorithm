def calc(index, check: list):
    if len(check) == n:
        return 0
    return max(calc(i, check + [i]) + abs(arr[index] - arr[i]) for i in range(n) if not i in check)


n = int(input())
arr = list(map(int, input().split()))

print(max(calc(i, [i]) for i in range(n)))
