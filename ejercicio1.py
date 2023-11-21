numer = int(input("Ingrese un número: "))
num = int(input("Ingrese otro número: "))
if numer > num:
    mensaje = f"{numer} es mayor que {num}"
elif num > numer:
    mensaje = f"{num} es mayor que {numer}"
else:
    mensaje = f"{numer} y {num} son iguales"
print(mensaje)