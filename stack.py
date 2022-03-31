while True:
    inputString = input("Enter a string: ")
    stack = []

    for char in inputString:
        stack.append(char)

    outputString = ""

    while len(stack) > 0:
        outputString += stack.pop()

    print(outputString)

#Try typing "reward"!
