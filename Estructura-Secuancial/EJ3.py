PartidosGanados = int(input("ingrese la cantidad de partidos ganados: "))
PartidosPerdidos = int(input("ingrese la cantidad de partidos perdidos: "))
PartidosEmpatados = int(input("ingrese la cantidad de partidos empatados: "))

puntos= (3 * PartidosGanados) + (2 * PartidosEmpatados) + (0 * PartidosPerdidos)

print("Puntos totales: ", puntos)