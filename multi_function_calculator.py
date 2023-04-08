# solve proportions
def proportions():
    print("One numerator or denominator must be Zero")
    n1 = int(input("Enter the first numerator: "))
    d1 = int(input("Enter the first denominator: "))
    n2 = int(input("Enter the second numerator: "))
    d2 = int(input("Enter the second denominator: "))

    if n2 == 0:
        answer = d2 * n1 / d1
        print("n2 = ", answer)

    if d2 == 0:
        answer = n2 * d1 / n1
        print("d2 = ", answer)

    if d1 == 0:
        answer = n2 * d2 / n2
        print("d1 = ", answer)

    if n1 == 0:
        answer = d1 * n2 / d2
        print('n1 = ', answer)


# solve for x in equations
def solve_for_x():
    import sympy
    from sympy import symbols
    from sympy.solvers import solve

    x = symbols('x')
    eq = input('Enter an equation to solve for x: 0 = ')
    print(len(solve(eq, x)))
    print("x = ", solve(eq, x)[0])


# factor square roots
def square():
    import math
    a = int(input("Enter the number: "))
    # from library import sqrt
    b = math.sqrt(a)
    print("The Square root of ", a, " is: ", b)


# convert decimals to fractions and percents
def deci():
    import math

    digits = input("Enter a decimal number to convert: ")
    exponent = int(len(digits)) - 1
    n = float(digits)

    # equation
    numerator = n * 10 ** exponent
    denominator = 10 ** exponent
    percent = n * 100

    print("The decimal is ", n)
    print("The fraction is ", numerator, "/", denominator)
    print("The percent is ", percent, " %")


# convert fractions to decimals and percents
def frac():
    import math
    first = int(input("Enter the numerator: "))
    second = int(input("Enter the denominator: "))

    # equation

    deci = float(first / second)
    percent = deci * 100

    print("The decimal is ", deci)
    print("The percent is ", percent, " %")


# convert percents to decimals and fractions
def percent():
    percent = float(input("Enter the percent value: "))

    # equation
    decimal = percent / 100
    fraction = percent / 100

    print(f"The decimal equivalent of {percent}% is {decimal}")
    print(f"{percent}% is equal to {fraction} as a decimal.")
    print(f"Simplified fraction: {int(fraction * 100)}/{100}")


# for loop
qst = str(input(
    "Hey! Welcome to the multi-function calculator \n Choose a Function: \n p for Proportion \n x for Solve for X \n sq for Square Root \n deci for The Convert of Decimals to fractions and percents \n frac for Convert Fractions to decimals and percents \n percent for Convert Percents to decimals and fractions \n"))
if qst == "p":
    proportions()
elif qst == "x":
    solve_for_x()
elif qst == "sq":
    square()
elif qst == "deci":
    deci()
elif qst == "frac":
    frac()
elif qst == "percent":
    percent()
else:
    print("Select the proper function")