# El area de RRHH de una empresa desea filtrar los CV de laos postulantes para un puesto vacante, el requisisto minimo es la edad pero los datos
# 0olo los tienen y las fechas de nacimeinto.


año_nacimiento_postulante   = int(input('ingrese su fecha de nacimiento:'))
año_actual                  = 2021
edad_postulante             = año_actual - año_nacimiento_postulante

print('la edad del postulante es :', edad_postulante)