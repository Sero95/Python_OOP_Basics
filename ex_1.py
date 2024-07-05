class Calculator:

    def __init__(self):  # will executing when i creat an objcts
        print("wellcom in our calculator")

    def Summ(self, x, y):
        print(self)  # look at address location
        return x + y

    def Mult(self, x, y):
        return x * y


process_1 = Calculator()
print(process_1.Summ(4, 5))
print(process_1.Mult(4, 5))
print(process_1)  # look at the out put the same location in memory with self


class Scientific(
    Calculator
):  # will print the constructor again and Calculator's method its available to use here

    def power(self, x, y):
        return x**y


x = Scientific()
print(x.power(4, 2))
print(x.Summ(2, 3))
print(x.Mult(2, 2))
