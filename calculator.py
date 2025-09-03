def Plus(a,b):
    return(a + b)
def Minus(a,b):
    return(a - b)

select = input("select 1 for Plus or select 2 for Minus : ")

a = float(input("First number : "))
b = float(input("Second number : "))

if select == "1":
    result = Plus(a,b)
    print(result)
elif select == "2":
    result = Minus(a,b)
    print(result)
else:
    print("Select Fail")
