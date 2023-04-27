from testclases import *
o1 = MyClass()
o2 = MySubclass(1, o1)


o1.my_function()
o1.añadir1()
o2.my_subfunctionx()
print(o1.x)
print(o2.x)

#Actualizamos o2 para que tenga la nueva x de o1
o2.updatex(o1)
print("ahora miramos:")
print(o2.x)
