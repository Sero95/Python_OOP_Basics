class Calculator:

    def __init__(self, Name):
        print(f"welcom {Name}")  # look at this statemnt

    def summ(self, x, y):
        return x + y


class Scientifice(Calculator):

    def __init__(self, Name):
        super(Scientifice, self).__init__(Name)  # super function to ineritance the constructor 
        print("Abo Bassam !")  # without super fun. will not print the parent constructor (welcom taisir)

    def Mult(self, x, y):
        return x * y


z = Scientifice("Taisir")
print(z.summ(4, 3))
print(z.Mult(4, 3))
