def title():
    print("-----------------------------------------------------------------------------------------------------")
    print("-------------------------------------SIMPLE CALCULATOR!!!-------------------------------------------- ")
    print("-----------------------------------------------------------------------------------------------------")


def menu():
    print("Which operation you wanna perform now:\n1.(+) ADDITION\n2.(-) SUBTRACTION\n3.(*) MULTIPLICATION\n4.(/) DIVISION\n5.EXIT")


def add(a,b):
    print(f"{a} + {b} =",a+b)
    print("RESULT IS: ",a+b)


def sub(a,b):
    print(f"{a} - {b} =",a-b)
    print("RESULT IS: ",a-b)


def mul(a,b):
    print(f"{a} * {b} =",a*b)
    print("RESULT IS: ",a*b)


def div(a,b):
    if b == 0:
        raise ValueError("Enter anyother for denominator rather than Zero.")
    else:
        print(f"{a} / {b} =",a/b)
        print("RESULT IS: ",a/b)


while True:

    title()

    menu()

    opt=input("Choose any option from the above: ")

    if opt == "1" or opt == "+" or opt.lower() == "addition":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        add(a,b)

    elif opt == "2" or opt == "-" or opt.lower() == "subtraction":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        sub(a,b)

    elif opt == "3" or opt == "*" or opt.lower() == "multiplication":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mul(a,b)

    elif opt == "4" or opt == "/" or opt.lower() == "division":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        div(a,b)

    elif opt == "5":
        print("Calculator Exited Successfully.")
        break

    else:
        print("Enter any valid option.")
        