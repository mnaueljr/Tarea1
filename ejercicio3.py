valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
valor3 = int(input("Ingrese el tercer valor: "))
suma = valor1 + valor2 + valor3
if suma % 7 == 0:
    mensaje = "La suma de los tres valores es múltiplo de 7."
else:
    mensaje = "La suma de los tres valores no es múltiplo de 7."
print(mensaje)