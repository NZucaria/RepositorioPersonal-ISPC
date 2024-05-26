#Prestamo de un banco#
#Desarrollar un programa que verifique la edad de una persona e indique si es posible otorgar
#un prestamo personal.
# SER MAYOR DE EDAD
# SER MENOR DE 65 AÑOS.
#En caso contrario no será posible otorgarle el crédito.

edad = int(input("Ingrese la edad de la persona: "))

if edad >= 18  and edad < 65:
    print("Felicidades! se le ha otorgado el credito")

else:
    print("No es posible dar el prestamo")
    