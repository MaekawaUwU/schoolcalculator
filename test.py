print("""calculator.exe starting...
type '7' for help""")
z=int(input("What do you want to do : "))
while z==8:
    x=int(input("Enter the first number : ")) # x c le premier nombre
    y=int(input("Enter the second number (or exponent) : ")) # y c la deuxieme nombre
    if z == 8:
        break
    elif z == 2:
        print(x-y)
    elif z == 3:
        print(x*y)
    elif z == 4:
        print(x/y)
    elif z == 5:
        import math
        print(math.sqrt(x))
        import math
        print(math.sqrt(y))
    elif z == 6:
        print(x**y)
    elif z == 7:
        print("""    1 = addition
        2 = substraction
        3 = multiplication
        4 = division
        5 = square root
        6 = exponent
        7 = list of command
        8 = shut it down
        9 = keep it open""")
    elif z==1:
        print(x+y)