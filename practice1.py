def fac(a):
    if a > 1:
        return a * fac(a-1)
    else:
        return 1
num = int(input("Enter a number: "))
print("The factoria of {1} is {0}".format(num, fac(num)))