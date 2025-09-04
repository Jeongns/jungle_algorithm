max_num = -1
n = 0
for i in range(1, 10):
    a = int(input())
    if max_num < a:
        max_num = a
        n = i

print(max_num)
print(n)