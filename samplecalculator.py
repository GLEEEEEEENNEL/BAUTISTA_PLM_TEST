print("gooooffy ahh callculator")

opera = input(" +/- =  ")

if opera == "+":
    print("addition")
    first = int(input("Enter a number 1: "))
    second = int(input("Enter a number 2: "))
    sum = first + second
    print("The sum of the two numbers is: ", sum)
elif opera == "-":
    print("subtraction")
    third = int(input("Enter a number 3: "))
    fourth = int(input("Enter a number 4: "))
    dif = third - fourth
    print("The difference of the two numbers is: ", dif)
else:
    print("dumdum")