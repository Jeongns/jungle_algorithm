for i in range(int(input())):
    def gcd(a, b):
        if not a % b:
            return b

        return gcd(b, a % b)


    a, b = map(int, input().split())
    print(gcd(*sorted([a, b], reverse=True)))