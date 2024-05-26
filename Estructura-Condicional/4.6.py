#realizar un programa en python que consulte el día de la semana en el que se está
#si es Sábado o Domingo imprima "¡FELIZ FIN DE SEMANA!". En el caso que sea otro dia indicar que se debe ir al colegio a estudiar.

dia = input("Ingrese el dia de la semana en el que está:")

if dia == "sabado" or dia == "domingo": 
    print("¡FELIZ FIN DE SEMANA!")
else: 
    print("Hoy se debe ir al colegio!")