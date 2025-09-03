def Plus(a,b):
    return(a + b)
def Minus(a,b):
    return(a - b)
def Multiply(a,b):
    return(a * b)
def Divide(a,b):
    return(a / b)

select = input(
    "Select Operation \n"
    "1: Plus\n"
    "2: Minus\n"
    "3: Multiply\n"
    "4: Divide\n"
    "Choose your Operation: "
    )

if select in ["1","2","3","4"]:

    a = float(input("First number : "))
    b = float(input("Second number : "))


    if select == "1":
        result = Plus(a,b)
        print(result)
    elif select == "2":
        result = Minus(a,b)
        print(result)
    elif select == "3":
        result  = Multiply(a,b)
        print(result)
    elif select == "4":
        result = Divide(a,b)
        print(result)

else:
    print("Selection Failed")