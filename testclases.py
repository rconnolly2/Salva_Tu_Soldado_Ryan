class MyClass:
    def __init__(self):
        self.x = 2

    def my_function(self):
        print("The value of x is:", self.x)

    def añadir1(self):
        self.x = self.x + 1



class MySubclass(MyClass):
    def __init__(self, y, objeto_myclass):
        super().__init__()
        self.y = y
        self.x = objeto_myclass.x

    def my_subfunctiony(self):
        print("The value of y is:", self.y)
        self.x = 0

    def my_subfunctionx(self):
        print("The value of x is:", self.x)

    def updatex(self, objeto_myclass):
        self.x = objeto_myclass.x





