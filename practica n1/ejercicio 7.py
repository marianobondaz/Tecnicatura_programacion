# Se desea calcular cuantos metros se deben recorrer para atravezar una plaza en diagonal,
# pero solo se conocen las distancias de las cuadras de ambos lados

from math import sqrt   #raiz cuadrada

lado_a      = int(input('ingrese el valor del lado A :'))
lado_B      = int(input('ingrese el valor del lado A :'))

diagonal    = int (sqrt(lado_a ** 2 + lado_b ** 2 ))

print ('la diagonal :', diagonal)
