for loop in range(0, int(input())):
    n, *arr = map(int, input().split())
    print(format((len(list(filter(lambda x: x > sum(arr) / len(arr), arr))) / len(arr)) * 100, '.3f')+"%")