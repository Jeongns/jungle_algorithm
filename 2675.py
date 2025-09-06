for loop in range(0, int(input())):
    r, s = input().split()
    print("".join(list(map(lambda x: x * int(r), s))))