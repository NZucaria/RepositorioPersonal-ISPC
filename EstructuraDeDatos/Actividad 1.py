# Pedir al usuario que ingrese 10 nombres de personas no repetidas, guardarlos en una lista y mostrarlos.
personas = []
for i in range(10):
    nombre = input("Ingrese el nombre de la persona {}: ".format(i + 1))
    while nombre in personas:
        print("El nombre ya ha sido ingresado. Intente nuevamente.")
        nombre = input("Ingrese el nombre de la persona {}: ".format(i + 1))
    personas.append(nombre)
print("Nombres de personas ingresados:", personas)

# Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo.
del personas[2]  # Eliminar la tercera persona
del personas[-1]  # Eliminar la última persona
personas.sort()  # Ordenar la lista
print("Nombres de personas después de eliminar y ordenar:", personas)

# Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.
persona_datos = {}
persona_datos['nombre'] = input("Ingrese el nombre de la persona: ")
persona_datos['apellido'] = input("Ingrese el apellido de la persona: ")
persona_datos['dni'] = input("Ingrese el DNI de la persona: ")
persona_datos['email'] = input("Ingrese el email de la persona: ")
persona_datos['fecha_nacimiento'] = input("Ingrese la fecha de nacimiento de la persona: ")
print("Datos de la persona:", persona_datos)

# En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos.
familia = {}
for i in range(4):
    persona = {}
    persona['nombre'] = input("Ingrese el nombre de la persona {}: ".format(i + 1))
    persona['apellido'] = input("Ingrese el apellido de la persona {}: ".format(i + 1))
    persona['dni'] = input("Ingrese el DNI de la persona {}: ".format(i + 1))
    persona['email'] = input("Ingrese el email de la persona {}: ".format(i + 1))
    persona['fecha_nacimiento'] = input("Ingrese la fecha de nacimiento de la persona {}: ".format(i + 1))
    familia['persona{}'.format(i + 1)] = persona
print("Datos de la familia:", familia)

# Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario. Luego mostrar los datos de la tupla.
n = int(input("Ingrese el valor de n: "))
numeros_pares = tuple(i for i in range(2, 2 * n + 1, 2))
print("Los primeros {} números pares son:".format(n), numeros_pares)

