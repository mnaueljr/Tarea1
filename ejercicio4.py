numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
mensaje = f"El promedio es {promedio}."
if promedio % 2 == 0:
    mensaje += " El promedio es un número par."
else:
    mensaje += " El promedio es un número impar."
print(mensaje)
