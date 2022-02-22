print("calculator.exe starting...")
print("""1 = No
2 = Yes""")
w=int(input("close the calculator : "))
while w==1:
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number (or exponent): "))
    print("""    1 = addition
    2 = substraction
    3 = multiplication
    4 = division
    5 = square root
    6 = exponent""")
    z=int(input("What do you want to do with these?: "))
    if z == 1:
            print(x+y)
    elif z == 2:
            print(x-y)
    elif z == 3:
            print(x*y)
    elif z == 4:
        print(x/y)
    elif z==5:
        import math
        print(math.sqrt(x))
        import math
        print(math.sqrt(y))
    elif z==6:
        print(x**y)
    print("""    1 = keep it open
    2 = shut it down""")
    w=int(input("calculator.exe will close, what you want to do: "))
    if w==2:
        break