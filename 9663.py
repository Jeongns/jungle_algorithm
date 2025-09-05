def n_queen(arr: list):
    if len(arr) == n:
        return 1
    attack_area = [False] * n
    for i in range(0, len(arr)):
        attack_area[arr[i]] = True
        if 0 <= arr[i] + (len(arr) - i) < n:
            attack_area[arr[i] + (len(arr) - i)] = True
        if 0 <= arr[i] - (len(arr) - i) < n:
            attack_area[arr[i] - (len(arr) - i)] = True

    result = 0
    for i in range(0, n):
        if not attack_area[i]:
            copy_arr = arr.copy()
            copy_arr.append(i)
            result += n_queen(copy_arr)

    return result


n = int(input())
print(n_queen([]))
