n, m = map(int, input().split())
d = [input() for i in range(n)]
b = [input() for i in range(m)]

result = list(set(d).intersection(b))
result.sort()

print(len(result))
print(*result)