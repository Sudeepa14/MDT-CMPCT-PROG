# Task 4 - factorial calculator
# factorial of n = n * (n-1) * (n-2) * ... * 1

if __name__ == '__main__':
    n = int(input("Input a number to calculate its factorial : "))

    # start at 1, not 0 - otherwise everything would multiply to 0
    ergebnis = 1

    for i in range(1, n + 1):
        ergebnis = ergebnis * i

    print("The factorial of " + str(n) + " is: " + str(ergebnis))
