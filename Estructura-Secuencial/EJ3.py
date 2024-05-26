#Un hincha de fútbol desea conocer la cantidad de puntos que su#

#equipo lleva acumulados en el campeonato, para ello recibe cada semana la#

#información de la cantidad total de partidos, desde el inicio del campeonato, que#

#el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado#

#recibe un punto, por cada partido ganado tres puntos y por los perdidos cero#

#puntos.#


PartidosGanados = int(input("ingrese la cantidad de partidos ganados: "))
PartidosPerdidos = int(input("ingrese la cantidad de partidos perdidos: "))
PartidosEmpatados = int(input("ingrese la cantidad de partidos empatados: "))

puntos= (3 * PartidosGanados) + (2 * PartidosEmpatados) + (0 * PartidosPerdidos)

print("Puntos totales: ", puntos)