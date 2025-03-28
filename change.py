import math

def change():
    expense = 23.75
    money = 100

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print()
    print("Vuelto")
    print()
    fractional, integer = math.modf(money - expense)
    print("Pesos:")
    print(round(integer))
    print("Centavos:")
    print(round(fractional * 100))
