# El entrenador de un equipo de basquet deasea determinar la eficacia en tiros de campo de un jugador "X"

tiros_totales   = int(input('ingrese el toral de tiros que realizo:'))
aciertos        = int(input('ingrese cuantos tiros acerto:'))

eficiencia      = float((tiros_totales / aciertos)*100)

print ('eficiencia %:', eficiencia)