class MyClass:
    def __init__(self):
        self.x = 2

    def my_function(self):
        print("The value of x is:", self.x)


class MySubclass(MyClass):
    def __init__(self, y):
        super().__init__()
        self.y = y

    def my_subfunction(self):
        print("The value of y is:", self.x)
        self.x = 0


o1 = MySubclass(1)

o1.my_function()
o1.my_subfunction()
o1.my_subfunction()
print(o1.x)

