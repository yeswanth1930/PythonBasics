class Calculator:

    def __int__(self):
        print("function declaration")
    def setNumber(self):
        self.number1 = input("Enter num 1::")
        self.number2 = input("Enter num 2::")
        self.opr = input("Enter opr::")
    def sum(self):
        return int(self.number1) + int(self.number2)
    def multiplication(self):
        return int(self.number1 )* int(self.number2)
    def div(self):
        return int(self.number1) / int(self.number2)
    def minus(self):
        return int(self.number1) -int (self.number2)
    def operations(self):
        if (self.opr == "+"):
           print(self.sum())
        elif (self.opr == "*"):
            print(self.multiplication())
        elif (self.opr == "-"):
            print(self.minus())
        elif (self.opr == "/"):
            print(self.div())



