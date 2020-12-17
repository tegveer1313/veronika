while True:
    x = int(input("enter your number"))
    a = input("enter maths opretion you want to do")
    y =int(input("enter your second number"))

    if a == '+':
        b = x + y
        print(b)
    elif a == '-':
        b = x - y
        print(b)
    elif a == '/':
        b = x / y
        print(b)
    elif a == '*':
        b = x * y
        print(b)
    elif a == '-':
        b = x - y
        print(b)
    elif a == '^':
        b = x ** y
        print(b)
    else:
        print("something went wrong")
else:
    print("progaram exited")