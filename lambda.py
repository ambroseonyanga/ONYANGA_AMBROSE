num = list((1,2,3,4,5))
for i in range(len(num)):
    square = lambda x: x*x
    print(square(num[i]))