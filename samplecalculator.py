print("gooooffy ahh callculator")

opera = input(" +/-/*// =  ")

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
elif opera == "*":
    print("multiplication")
    fifth = int(input("Enter a number 5: "))
    sixth = int(input("Enter a number 6: "))
    multi = fifth * sixth
    print("the product of the two number is: ", multi)
elif opera == "/":
    print("division")
    seventh = int(input("Enter a number 7: "))
    eightn = int(input("Enter a number 8: "))
    div = seventh / eightn
    print("the quotient of the two number is: ", div)
else:
    print("dumdum")