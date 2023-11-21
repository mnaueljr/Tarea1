valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
valor3 = int(input("Ingrese el tercer valor: "))
if valor1 > valor2 and valor1 > valor3:
    mensaje = f"{valor1} es el mayor valor."
elif valor2 > valor1 and valor2 > valor3:
    mensaje = f"{valor2} es el mayor valor."
elif valor3 > valor1 and valor3 > valor2:
    mensaje = f"{valor3} es el mayor valor."
print(mensaje);