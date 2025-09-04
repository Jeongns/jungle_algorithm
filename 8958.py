for loop in range(0, int(input())):
    xo = input()
    score = 0
    n = 1

    for i in xo:
        if i == "X":
            n = 1
            continue
        score += n
        n += 1

    print(score)
