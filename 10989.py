import sys

arr = [0] * 10001
for i in range(0, int(int(sys.stdin.readline().strip()))):
    arr[int(sys.stdin.readline().strip())] += 1

for i in range(0, len(arr)):
    if arr[i] == 0:
        continue
    for j in range(0, arr[i]):
        print(i)