def calc():
    for i in range(9):
        for j in range(i, 9):
            if sum(arr) - arr[i] - arr[j] == 100:
                for k in range(9):
                    if k == j or k == i:
                        continue
                    print(arr[k])
                return

arr = []
for i in range(9):
    arr.append(int(input()))

arr.sort()

calc()
