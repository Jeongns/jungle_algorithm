import math

is_prime = [True] * 10001
is_prime[1] = False

for i in range(2, int(math.sqrt(len(is_prime)))):
    if not is_prime[i]:
        continue
    for j in range(i * 2, len(is_prime), i):
        is_prime[j] = False


for loop in range(0, int(input())):
    n = int(input())
    gb_num = 0
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            gb_num = i

    print(gb_num, n - gb_num)
