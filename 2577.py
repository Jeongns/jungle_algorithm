n = int(input()) * int(input()) * int(input())
arr = [0] * 10
for i in str(n):
    arr[int(i)] += 1

print("\n".join(map(str, arr)))