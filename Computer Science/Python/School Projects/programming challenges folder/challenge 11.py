def getInfo():
    gate = input("Enter logic gate: ")
    input1 = int(input("Enter first input: "))
    input2 = int(input("Enter second input: "))

    if gate.lower() == "and":
        if input1 == 1 and input2 == 1:
            return 1
        else:
            return 0
    if gate.lower() == "or":
        if input1 == 1 or input2 == 1:
            return 1
        else:
            return 0
    if gate.lower() == "xor":
        if input1 == 1 ^ input2 == 1:
            return 1
        else:
            return 0
while True:
    print("The logic gate will return as", getInfo())
