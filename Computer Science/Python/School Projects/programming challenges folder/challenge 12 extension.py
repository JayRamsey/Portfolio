n = 0
facList = []
while not n > 0:
    n = int(input("Enter number: "))

for i in range(1, (n // 2 + 1)):
    if n % i == 0:
        facList += str(i)
        print(i, "is a factor of", n)
