class Calculator:
    # if i dont call constructor as an object will not executed
    def __init__(self, Name):
        print("welcom to calculator: ")
        # if constructor consist argument (Name)should written in objects creation


class A:  # parents class main class super class

    def Summ(self, x, y):
        print("im in A")  # dont put this print out of the method
        return x + y


class B:

    def Summ(self, x, y):
        print("im in B")  # dont put this print fuc. out of the  method
        return x + y


class C(B):

    def Multi(self, x, y):
        return x * y


class D(C, A, Calculator):  # D is child class drived class subclass
    # will iterihance from the C first if dont found will search in A

    def Sub(self, x, y):
        return x - y


z = D("Taisir")
z.Summ(4, 3)
