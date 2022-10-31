def factorial(n):
    if (n==0):
        return 1
    else:
        return n * factorial(n-1)


def number_of_digits(n):
    number = 0
    while (n>0):
        number += 1
        n = n//10
    return number


def report():
    for i in range(101):
        print(f"{i : >3}! is {(str(number_of_digits(factorial(i))))}  digits long")


report()
