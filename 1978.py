input()
nums = map(int, input().split())
result = 0
for i in nums:
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime and i > 1:
        result += 1
print(result)
