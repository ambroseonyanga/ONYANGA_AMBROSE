age = int(input("Enter your age: "))
try:
    if age <18:
        raise ValueError("\033[91mYou are below age to enter into the cinema!\033[0m")
    else:
        print("You can enter the cinema because you are above age!")
except ValueError as e:
    print(e)
print("\033[92mCode has run successfully\033[0m")