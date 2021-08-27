number1=int(input("enter number1 ::"))
number2=int(input("enter number2 ::"))
operator=input("enter operator ::")
def addition(x,y):
    return x+y
def mul(x,y):
    return x*y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y


if (operator == "+"):
    print("Sum ::"+str(addition(number1,number2)))
elif(operator == "-"):
    print(sub(number1,number2))
elif(operator == "*"):
    print(mul(number1,number2))
elif(operator == "/"):
    print(div(number1,number2))








print(int(number1),int(number2),str(operator))