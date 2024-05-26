
#Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido entre 1 y 10. Por ejemplo para el 3 debería aparecer como salida:

print("5. TABLA DE MULTIPLICAR - SOLUCIÓN MIENTRAS (while)")

numero = int(input("Ingresá un número entre 1 y 10: "))
i = 1

while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1
    
print("5. TABLA DE MULTIPLICAR - SOLUCIÓN PARA (for)")

numero = int(input("Ingresá un número entre 1 y 10: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")