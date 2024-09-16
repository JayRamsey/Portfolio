while True:
    n = 0
    while not n > 0:
        n = int(input("Enter number: "))

    for i in range(1, (n // 2 + 1)):
        if n % i == 0:
            print(i, "is a factor of", n)
